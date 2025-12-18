// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Escrow {
    address public buyer;
    address public seller;
    bool public released;

    constructor(address _seller) {
        buyer = msg.sender;
        seller = _seller;
    }

    function release() public {
        require(msg.sender == buyer);
        released = true;
        payable(seller).transfer(address(this).balance);
    }

    receive() external payable {}
}
