/*global process*/

const { ethers } = require("hardhat");

async function main() {
    const fs = require("fs");
    const globalsFile = "globals.json";
    const dataFromJSON = fs.readFileSync(globalsFile, "utf8");
    let parsedData = JSON.parse(dataFromJSON);
    const providerName = parsedData.providerName;
    const gasPriceInGwei = parsedData.gasPriceInGwei;
    const growRegistryName = parsedData.growRegistryName;
    const growRegistrySymbol = parsedData.growRegistrySymbol;
    const baseURI = parsedData.baseURI;

    const signers = await ethers.getSigners();
    const EOA = signers[0];

    // EOA address
    const deployer = await EOA.getAddress();
    console.log("EOA is:", deployer);

    // Transaction signing and execution
    console.log("1. EOA to deploy GrowRegistry");
    const gasPrice = ethers.utils.parseUnits(gasPriceInGwei, "gwei");
    const ServiceRegistry = await ethers.getContractFactory("GrowRegistry");
    console.log("You are signing the following transaction: GrowRegistry.connect(EOA).deploy()");
    const growRegistry = await ServiceRegistry.connect(EOA).deploy(growRegistryName, growRegistrySymbol, baseURI, { gasPrice });
    const result = await growRegistry.deployed();

    // Transaction details
    console.log("Contract deployment: GrowRegistry");
    console.log("Contract address:", growRegistry.address);
    console.log("Transaction:", result.deployTransaction.hash);
    // Wait half a minute for the transaction completion
    await new Promise(r => setTimeout(r, 30000));

    // Writing updated parameters back to the JSON file
    parsedData.growRegistryAddress = growRegistry.address;
    fs.writeFileSync(globalsFile, JSON.stringify(parsedData));

    // Contract verification
    if (parsedData.contractVerification) {
        const execSync = require("child_process").execSync;
        execSync("npx hardhat verify --constructor-args scripts/deployment/verify_01_grow_registry.js --network " + providerName + " " + growRegistry.address, { encoding: "utf-8" });
    }
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
