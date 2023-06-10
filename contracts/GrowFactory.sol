// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {GenericManager} from "../lib/autonolas-registries/contracts/GenericManager.sol";

interface IGrowRegistry {
    /// @dev Creates a grow.
    /// @param growOwner Owner of the grow.
    /// @param grower Grower address.
    /// @param growHash IPFS CID hash of the grow metadata.
    /// @return growId The id of a minted grow.
    function create(address growOwner, address grower, bytes32 growHash) external returns (uint256 growId);
}

/// @title Grow Factory - Periphery smart contract for managing grow
contract GrowFactory is GenericManager {
    // Grow factory version number
    string public constant VERSION = "1.0.0";

    // Grow registry address
    address public immutable growRegistry;

    constructor(address _growRegistry) {
        growRegistry = _growRegistry;
        owner = msg.sender;
    }

    /// @dev Creates a grow.
    /// @param growOwner Owner of the grow.
    /// @param grower Grower address.
    /// @param growHash IPFS CID hash of the grow metadata.
    /// @return growId The id of a created grow.
    function create(
        address growOwner,
        address grower,
        bytes32 growHash
    ) external returns (uint256 growId)
    {
        // Check if the creation is paused
        if (paused) {
            revert Paused();
        }

        growId = IGrowRegistry(growRegistry).create(growOwner, grower, growHash);
    }
}
