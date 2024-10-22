// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint) private balances;

    function create_account() public payable returns(string memory) {
        require(balances[msg.sender] == 0, "Account already created!");
        balances[msg.sender] = msg.value;
        return "Account created";
    }

    function deposit() public payable returns(string memory) {
        require(msg.value > 0, "Amount should be greater than 0");
        balances[msg.sender] += msg.value;
        return "Amount deposited successfully";
    }

    function withdraw(uint amount) public returns(string memory) {
        require(amount > 0, "Amount should be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        return "Amount withdrawn successfully";
    }

    function account_balance() public view returns(uint) {
        return balances[msg.sender];
    }
}
