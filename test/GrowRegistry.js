/*global describe, context, beforeEach, it*/

const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("GrowRegistry", function () {
    let growRegistry;
    let reentrancyAttacker;
    let signers;
    const growHash = "0x" + "9".repeat(64);
    const growHash1 = "0x" + "1".repeat(64);
    const growHash2 = "0x" + "2".repeat(64);
    const AddressZero = "0x" + "0".repeat(40);
    const ZeroBytes32 = "0x" + "0".repeat(64);
    beforeEach(async function () {
        const GrowRegistry = await ethers.getContractFactory("GrowRegistry");
        growRegistry = await GrowRegistry.deploy("grow", "GROW", "https://localhost/grow/");
        await growRegistry.deployed();

        const ReentrancyAttacker = await ethers.getContractFactory("ReentrancyAttacker");
        reentrancyAttacker = await ReentrancyAttacker.deploy(growRegistry.address);
        await reentrancyAttacker.deployed();

        signers = await ethers.getSigners();
    });

    context("Initialization", async function () {
        it("Checking for arguments passed to the constructor", async function () {
            expect(await growRegistry.name()).to.equal("grow");
            expect(await growRegistry.symbol()).to.equal("GROW");
            expect(await growRegistry.baseURI()).to.equal("https://localhost/grow/");
        });

        it("Should fail when checking for the token id existence", async function () {
            const tokenId = 0;
            expect(await growRegistry.exists(tokenId)).to.equal(false);
        });

        it("Should fail when trying to change the growFactory from a different address", async function () {
            await expect(
                growRegistry.connect(signers[1]).changeManager(signers[1].address)
            ).to.be.revertedWithCustomError(growRegistry, "OwnerOnly");
        });

        it("Setting the base URI", async function () {
            await growRegistry.setBaseURI("https://localhost2/grow/");
            expect(await growRegistry.baseURI()).to.equal("https://localhost2/grow/");
        });
    });

    context("Grow creation", async function () {
        it("Should fail when creating an grow without a growFactory", async function () {
            const user = signers[2];
            await expect(
                growRegistry.create(user.address, growHash)
            ).to.be.revertedWithCustomError(growRegistry, "ManagerOnly");
        });

        it("Should fail when creating an grow with a zero owner address", async function () {
            const growFactory = signers[1];
            await growRegistry.changeManager(growFactory.address);
            await expect(
                growRegistry.connect(growFactory).create(AddressZero, growHash)
            ).to.be.revertedWithCustomError(growRegistry, "ZeroAddress");
        });

        it("Should fail when creating an grow with a zero owner address", async function () {
            const growFactory = signers[1];
            const user = signers[2];
            await growRegistry.changeManager(growFactory.address);
            await expect(
                growRegistry.connect(growFactory).create(user.address, ZeroBytes32)
            ).to.be.revertedWithCustomError(growRegistry, "ZeroValue");
        });

        it("Token Id=1 after first successful grow creation must exist ", async function () {
            const growFactory = signers[1];
            const user = signers[2];
            const tokenId = 1;
            await growRegistry.changeManager(growFactory.address);
            await growRegistry.connect(growFactory).create(user.address, growHash);
            expect(await growRegistry.balanceOf(user.address)).to.equal(1);
            expect(await growRegistry.exists(tokenId)).to.equal(true);

            // Check the token URI
            const baseURI = "https://localhost/grow/";
            const cidPrefix = "f01701220";
            expect(await growRegistry.tokenURI(1)).to.equal(baseURI + cidPrefix + "9".repeat(64));

            // Try to return a token URI of a non-existent unit Id
            await expect(
                growRegistry.tokenURI(2)
            ).to.be.revertedWithCustomError(growRegistry, "GrowNotFound");
        });

        it("Catching \"Transfer\" event log after successful creation of an grow", async function () {
            const growFactory = signers[1];
            const user = signers[2];
            await growRegistry.changeManager(growFactory.address);
            const grow = await growRegistry.connect(growFactory).create(user.address, growHash);
            const result = await grow.wait();
            expect(result.events[0].event).to.equal("Transfer");
        });
    });

    context("Updating hashes", async function () {
        it("Should fail when the grow does not belong to the owner or IPFS hash is invalid", async function () {
            const growFactory = signers[1];
            const user = signers[2];
            const user2 = signers[3];
            await growRegistry.changeManager(growFactory.address);
            await growRegistry.connect(growFactory).create(user.address,
                growHash);
            await growRegistry.connect(growFactory).create(user2.address,
                growHash1);
            await expect(
                growRegistry.updateHash(1, growHash2)
            ).to.be.revertedWithCustomError(growRegistry, "GrowerOnly");
            await expect(
                growRegistry.updateHash(2, growHash2)
            ).to.be.revertedWithCustomError(growRegistry, "GrowerOnly");
            await growRegistry.connect(user).updateHash(1, growHash2);
        });

        it("Update hash, get component hashes", async function () {
            const growFactory = signers[1];
            const user = signers[2];
            await growRegistry.changeManager(growFactory.address);
            await growRegistry.connect(growFactory).create(user.address, growHash);

            // Try to update with a zero hash
            await expect(
                growRegistry.connect(user).updateHash(1, ZeroBytes32)
            ).to.be.revertedWithCustomError(growRegistry, "ZeroValue");

            // Update hashes
            await growRegistry.connect(user).updateHash(1, growHash1);
            expect(await growRegistry.mapGrowIdHashes(1)).to.equal(growHash1);
            await growRegistry.connect(user).updateHash(1, growHash2);
            expect(await growRegistry.mapGrowIdHashes(1)).to.equal(growHash2);
        });
    });

    context("Reentrancy attack", async function () {
        it("Reentrancy attack by the manager during the service creation", async function () {
            // Change the manager to the attacker contract address
            await growRegistry.changeManager(reentrancyAttacker.address);

            // Simulate the reentrancy attack
            await expect(
                reentrancyAttacker.createBadAgent(reentrancyAttacker.address, growHash)
            ).to.be.revertedWithCustomError(growRegistry, "ReentrancyGuard");
        });
    });
});
