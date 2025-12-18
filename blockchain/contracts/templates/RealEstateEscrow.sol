pragma solidity ^0.8.20;

contract RealEstateEscrow {
    address public buyer;
    address public seller;
    uint256 public price;
    bool public closed;

    constructor(address _seller) {
        seller = _seller;
        buyer = msg.sender;
    }

    function deposit() external payable {
        require(msg.sender == buyer);
        price += msg.value;
    }

    function close() external {
        require(msg.sender == buyer);
        closed = true;
        payable(seller).transfer(price);
    }
}
