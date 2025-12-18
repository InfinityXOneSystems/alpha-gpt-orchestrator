pragma solidity ^0.8.20;

contract DAOApproval {
    mapping(address => bool) public voters;
    uint256 public approvals;
    uint256 public threshold = 2;

    constructor(address[] memory _voters) {
        for (uint i=0;i<_voters.length;i++){
            voters[_voters[i]] = true;
        }
    }

    function approve() external {
        require(voters[msg.sender]);
        approvals++;
    }

    function approved() external view returns (bool) {
        return approvals >= threshold;
    }
}
