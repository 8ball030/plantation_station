/*global describe, context, beforeEach, it*/

const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("GrowFactory", function () {
    let growRegistry;
    let growFactory;
    let signers;
    const growHash = "0x" + "5".repeat(64);
    const price = 1;
    beforeEach(async function () {
        const GrowRegistry = await ethers.getContractFactory("GrowRegistry");
        growRegistry = await GrowRegistry.deploy("grow", "GROW", "https://localhost/grow/");
        await growRegistry.deployed();

        const GrowFactory = await ethers.getContractFactory("GrowFactory");
        growFactory = await GrowFactory.deploy(growRegistry.address);
        await growFactory.deployed();

        signers = await ethers.getSigners();
    });

    context("Initialization", async function () {
        it("Checking for arguments passed to the constructor", async function () {
            expect(await growFactory.growRegistry()).to.equal(growRegistry.address);
        });

        it("Pausing and unpausing", async function () {
            const user = signers[3];

            // Try to pause not from the owner of the service manager
            await expect(
                growFactory.connect(user).pause()
            ).to.be.revertedWithCustomError(growFactory, "OwnerOnly");

            // Pause the contract
            await growFactory.pause();

            // Try minting when paused
            await expect(
                growFactory.create(user.address, growHash)
            ).to.be.revertedWithCustomError(growFactory, "Paused");

            // Try to unpause not from the owner of the service manager
            await expect(
                growFactory.connect(user).unpause()
            ).to.be.revertedWithCustomError(growFactory, "OwnerOnly");

            // Unpause the contract
            await growFactory.unpause();

            // Mint an grow
            await growRegistry.changeManager(growFactory.address);
            await growFactory.create(user.address, growHash);
        });
    });
});
