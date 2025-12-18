pragma solidity ^0.8.20;

/*
  TESTNET ONLY
  Records AI instance creation + lineage
  NO FUNDS
*/

contract AIReplicationRegistry {

    struct AIInstance {
        address creator;
        string imageHash;
        uint256 createdAt;
        string purpose;
    }

    AIInstance[] public instances;

    event AIReplicated(
        address indexed creator,
        uint256 indexed id,
        string imageHash,
        string purpose
    );

    function replicate(string memory imageHash, string memory purpose) public {
        instances.push(AIInstance(
            msg.sender,
            imageHash,
            block.timestamp,
            purpose
        ));
        emit AIReplicated(msg.sender, instances.length - 1, imageHash, purpose);
    }

    function totalInstances() public view returns (uint256) {
        return instances.length;
    }
}
