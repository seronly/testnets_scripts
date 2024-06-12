from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3, HTTPProvider

from pydantic import BaseModel


class Wallet(BaseModel):

    def __init__(self):
        account: LocalAccount = Account.create()
        self.address: str = account.address
        self.private_key: str = account.privateKey.hex()

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.address=!r}, {self.address=!r})"

    def from_private_key(self, private_key: str):
        account: LocalAccount = Client.web3.eth.account.from_key(private_key)
        self.address = account.address
        self.private_key = private_key


class Client(BaseModel):
    rpc_url: str = "https://testnet-rpc.atleta.network"
    chain_id: int = 2340
    web3: Web3 = Web3(HTTPProvider(rpc_url))
