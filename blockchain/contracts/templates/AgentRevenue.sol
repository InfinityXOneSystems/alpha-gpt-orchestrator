pragma solidity ^0.8.20;

contract AgentRevenue {
    mapping(string => uint256) public revenue;

    function record(string memory agent, uint256 amount) public {
        revenue[agent] += amount;
    }

    function get(string memory agent) public view returns (uint256) {
        return revenue[agent];
    }
}
