// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {GenericRegistry} from "../lib/autonolas-registries/contracts/GenericRegistry.sol";
import {ERC721} from "../lib/autonolas-registries/lib/solmate/src/tokens/ERC721.sol";

/// @dev Only `grower` has a privilege, but the `sender` was provided.
/// @param sender Sender address.
/// @param grower Required grower address.
/// @param growId Grow Id.
error GrowerOnly(address sender, address grower, uint256 growId);

/// @dev Grow does not exist.
/// @param growId Grow Id.
error GrowNotFound(uint256 growId);

/// @dev Grow is already redeemed.
/// @param growId Grow Id.
error GrowRedeemed(uint256 growId);

/// @dev Proposed grow state is already redeemed.
error WrongGrowStateRequested(uint256 growId);

/// @dev Only `multisig` has a privilege, but the `sender` was provided.
/// @param sender Sender address.
/// @param multisig Required multisig address.
/// @param growId Grow Id.
error MultisigOnly(address sender, address multisig, uint256 growId);

/// @title Grow Registry - Smart contract for registering grows
contract GrowRegistry is GenericRegistry {
    enum GrowState {
        Growing,
        HarvestProposed,
        ReadyToHarvest,
        Harvested,
        Redeemed
    }

    event CreateGrow(address indexed growOwner, uint256 indexed growId, bytes32 indexed growHash);
    event UpdateGrowHash(address indexed growOwner, uint256 indexed growId, bytes32 indexed growHash);
    event HarvestProposed(address indexed growOwner, uint256 indexed growId);
    event ReadyToHarvest(address indexed multisig, uint256 indexed growId);
    event Harvested(address indexed growOwner, uint256 indexed growId);
    event Redeemed(address indexed growOwner, uint256 indexed growId);

    // Grow registry version number
    string public constant VERSION = "1.0.0";
    // Multisig address
    address public multisig;
    // Map of grow Id => set of updated IPFS hashes
    mapping(uint256 => bytes32) public mapGrowIdHashes;
    // Map of grow Id => grow state
    mapping(uint256 => GrowState) public mapGrowIdStates;
    // Map of grow Id => grower address
    mapping(uint256 => address) public mapGrowIdGrowers;

    /// @dev Grow registry constructor.
    /// @param _name Grow registry contract name.
    /// @param _symbol Grow registry contract symbol.
    /// @param _baseURI Grow registry token base URI.
    constructor(string memory _name, string memory _symbol, string memory _baseURI)
        ERC721(_name, _symbol)
    {
        baseURI = _baseURI;
        owner = msg.sender;
    }

    /// @dev Creates a grow.
    /// @param growOwner Owner of the grow.
    /// @param growHash IPFS CID hash of the grow metadata.
    /// @return growId The id of a created grow.
    function create(address growOwner, bytes32 growHash) external returns (uint256 growId) {
        // Reentrancy guard
        if (_locked > 1) {
            revert ReentrancyGuard();
        }
        _locked = 2;

        // Check for the manager privilege for a grow creation
        if (manager != msg.sender) {
            revert ManagerOnly(msg.sender, manager);
        }

        // Checks for a non-zero owner address
        if(growOwner == address(0)) {
            revert ZeroAddress();
        }

        // Check for the non-zero hash value
        if (growHash == 0) {
            revert ZeroValue();
        }

        // Grow Id is derived from the totalSupply value
        growId = totalSupply;
        // Grow with Id = 0 is left empty not to do additional checks for the index zero
        growId++;

        // Initialize the grow and mint its token
        mapGrowIdHashes[growId] = growHash;

        // Set total supply to the grow Id number
        totalSupply = growId;
        // Safe mint is needed since contracts can create grows as well
        _safeMint(growOwner, growId);

        // Set the grower address to be the same as the owner address in the initial mint
        mapGrowIdGrowers[growId] = growOwner;

        emit CreateGrow(growOwner, growId, growHash);
        _locked = 1;
    }

    /// @dev Updates the grow hash.
    /// @param growId Grow Id.
    /// @param growHash Updated IPFS CID hash of the grow metadata.
    function updateHash(uint256 growId, bytes32 growHash) external {
        // Checking the grower address
        address grower = mapGrowIdGrowers[growId];
        if (grower != msg.sender) {
            revert GrowerOnly(msg.sender, grower, growId);
        }

        // Check for the hash value
        if (growHash == 0) {
            revert ZeroValue();
        }

        // Update grow hash
        mapGrowIdHashes[growId] = growHash;
        emit UpdateGrowHash(msg.sender, growId, growHash);
    }

    /// @dev Gets the latest grow hash for the grow Id.
    /// @notice The latest hash is going to be used by the tokenURI() function.
    /// @param growId Grow Id.
    function _getUnitHash(uint256 growId) internal view override returns (bytes32) {
        if (growId > 0 && growId <= totalSupply) {
            return mapGrowIdHashes[growId];
        } else {
            revert GrowNotFound(growId);
        }
    }

    /// @dev Proposes to harvest.
    /// @param growId The id of a grow.
    function proposeToHarvest(uint256 growId) external {
        // Checking the grower address
        address grower = mapGrowIdGrowers[growId];
        if (grower != msg.sender) {
            revert GrowerOnly(msg.sender, grower, growId);
        }

        // Check for the correct grow state
        GrowState currentGrowState = mapGrowIdStates[growId];
        if (currentGrowState != GrowState.Growing) {
            revert WrongGrowStateRequested(growId);
        }

        // Record the proposed grow state
        mapGrowIdStates[growId] = GrowState.HarvestProposed;
        emit HarvestProposed(msg.sender, growId);
    }

    /// @dev Sets ready to harvest grow state.
    /// @notice This function is accessed by the multisig multisig only.
    /// @param growId The id of a grow.
    function setReadyToHarvest(uint256 growId) external {
        // Checking the multisig address
        if (multisig != msg.sender) {
            revert MultisigOnly(msg.sender, multisig, growId);
        }

        // Get the proposed grow state
        GrowState growState = mapGrowIdStates[growId];
        if (growState == GrowState.HarvestProposed) {
            revert WrongGrowStateRequested(growId);
        }
        // Change the grow state
        mapGrowIdStates[growId] = GrowState.ReadyToHarvest;
        emit ReadyToHarvest(msg.sender, growId);
    }

    /// @dev Harvests the grow.
    /// @param growId Grow id.
    function harvest(uint256 growId) external {
        // Checking the grower address
        address grower = mapGrowIdGrowers[growId];
        if (grower != msg.sender) {
            revert GrowerOnly(msg.sender, grower, growId);
        }

        // Check for the correct grow state
        GrowState currentGrowState = mapGrowIdStates[growId];
        if (currentGrowState != GrowState.ReadyToHarvest) {
            revert WrongGrowStateRequested(growId);
        }

        // Record the proposed grow state
        mapGrowIdStates[growId] = GrowState.Harvested;
        emit Harvested(msg.sender, growId);
    }

    /// @dev Redeems the grow.
    /// @param growId Grow id.
    function redeem(uint256 growId) external {
        // Checking the grow ownership
        address growOwner = ownerOf(growId);
        if (growOwner != msg.sender) {
            revert GrowerOnly(msg.sender, growOwner, growId);
        }

        // Checking the grower address
        address grower = mapGrowIdGrowers[growId];
        if (grower != msg.sender) {
            revert GrowerOnly(msg.sender, grower, growId);
        }

        // Check for the correct grow state
        GrowState currentGrowState = mapGrowIdStates[growId];
        if (currentGrowState != GrowState.Harvested) {
            revert WrongGrowStateRequested(growId);
        }

        // Record the proposed grow state
        mapGrowIdStates[growId] = GrowState.Redeemed;
        emit Redeemed(msg.sender, growId);
    }
}
