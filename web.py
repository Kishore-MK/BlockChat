from requests import get
import os
from dotenv  import load_dotenv
from web3 import Web3
load_dotenv()
val = os.getenv("apikey")
private = os.getenv("private")
infura_url = 'https://mainnet.infura.io/v3/4576a1b79c004deea16a86c964e7d889'
w3 = Web3(Web3.HTTPProvider(infura_url))

public='0xECc6947219d822C7a41993d671C97D8c39EA57AD'
recv='0xc8b4fd83E9A010Cc6C494D06a21c447a992C1048'
abi=[
  {
    "constant": True,
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "name": "",
        "type": "string"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "decimals",
    "outputs": [
      {
        "name": "",
        "type": "uint8"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "name": "balance",
        "type": "uint256"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "name": "",
        "type": "string"
      }
    ],
    "payable": False,
    "type": "function"
  }
]
def get_balance(infura_url,user_address):
       contract_address = "0xc2132D05D31c914a87C6611C10748AEb04B58e8F"
       
       web3 = Web3(Web3.HTTPProvider(infura_url))
       contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address.lower()), abi=abi)
       balance = contract.functions.balanceOf(Web3.to_checksum_address(user_address.lower())).call()
       return balance
# a1 = get_balance(infura_url,public)
# print(a1)
add1 = w3.to_checksum_address(public)
add2 = w3.to_checksum_address(recv)

nonce = w3.eth.get_transaction_count(add1)
txn = {
       'nonce':nonce,
       'to':recv,
       'value':w3.to_wei('0.0001', 'ether'),
       'gas':21000,
       'gasPrice':w3.to_wei('10','gwei')
}
signed_tx = w3.eth.account.sign_transaction(txn,private)
# print(signed)
sent = w3.eth.send_raw_transaction(signed_tx.rawTransaction)