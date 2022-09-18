// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts@4.7.3/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts@4.7.3/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts@4.7.3/access/Ownable.sol";
import "@openzeppelin/contracts@4.7.3/utils/Counters.sol";

contract IMLY is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    uint256 public MINT_PRICE = 0 ether;
    uint256 public MAX_SUPPLY = 10000;

    constructor() ERC721("IMLY", "MTK") {

        _tokenIdCounter.increment();
    }

    function withdraw() public onlyOwner() {
        require(address(this).balance > 0, "Balance is zero");
        payable(owner()).transfer(address(this).balance);
    }

    function _baseURI() internal pure override returns (string memory) {
        return "ipfs://happyMonkeyBaseURI/";
    }

    function safeMint(address to) public payable {
        // require(totalSupply < MAX_SUPPLY, "No more tokens to be minted");
        require(msg.value >= MINT_PRICE, "Not enough ether sent");
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}

/*
{
    owner: 0x3883cA5D1C46656595BC02a903Ae070826c6F705;
}
*/