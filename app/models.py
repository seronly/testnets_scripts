from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3, HTTPProvider

import logging
from pydantic import BaseModel

from app.db import add_wallet


class Wallet(BaseModel, extra="allow"):

    address: str
    private_key: str

    def __init__(self, address: str, private_key: str):
        super().__init__(
            address=address,
            private_key=private_key,
        )
        self.checksum_address = Web3.to_checksum_address(address)

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.address=!r}, {self.private_key=!r})"


class Client:

    rpc_url: str = "https://testnet-rpc.atleta.network"
    web3: Web3 = Web3(HTTPProvider(rpc_url))
    chain_id: int = web3.eth.chain_id
    wallets: list[Wallet] = []

    @staticmethod
    def add_wallet(wallet: Wallet) -> None:
        Client.wallets.append(wallet)

    @staticmethod
    def generate_wallets(count: int) -> None:
        for i in range(count):
            wallet: Wallet = Client.create_wallet()
            logging.info(
                f"Wallet with address {wallet.address}, private key {wallet.private_key} added"
            )
            add_wallet(wallet.checksum_address, wallet.private_key)

    @staticmethod
    def create_wallet() -> Wallet:
        account = Account.create()
        address: str = account.address
        private_key: str = account.key.hex()
        return Wallet(address=address, private_key=private_key)

    @staticmethod
    def get_wallet_from_private_key(private_key: str) -> Wallet:
        account: LocalAccount = Client.web3.eth.account.from_key(private_key)
        address = account.address
        private_key = private_key
        return Wallet(address=address, private_key=private_key)

    @staticmethod
    def send_n_sign_transaction(
        from_wallet: Wallet,
        to_address: str,
        value: int,
        gas: int,
        max_fee_per_gas: int,
        max_priority_fee_per_gas: int,
    ):
        transaction = {
            "from": from_wallet.address,
            "to": to_address,
            "value": value,
            "nonce": Client.web3.eth.get_transaction_count(from_wallet.address),
            "gas": gas,
            "maxFeePerGas": max_fee_per_gas,
            "maxPriorityFeePerGas": max_priority_fee_per_gas,
            "chainId": Client.chain_id,
        }
        signed = Client.web3.eth.account.sign_transaction(
            transaction, from_wallet.private_key
        )
        tx_hash = Client.web3.eth.send_raw_transaction(signed.rawTransaction)

        tx = Client.web3.eth.get_transaction(tx_hash)
        logging.info(tx)
        assert tx["from"] == from_wallet.address
