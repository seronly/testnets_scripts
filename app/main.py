from web3 import Web3, EthereumTesterProvider, HTTPProvider
from eth_account import Account
from eth_account.signers.local import LocalAccount
import logging

logger = logging.getLogger("web3.HTTPProvider")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
)

rpc_url = "https://testnet-rpc.atleta.network"
chain_id = 2340
web3 = Web3(HTTPProvider(rpc_url))

null_address = "0x0000000000000000000000000000000000000000"


def create_wallet():
    account = Account.create()
    address = account.address
    private_key = account.privateKey.hex()
    print(f"Новый кошелек создан. Адрес: {address}, Приватный ключ: {private_key}")


def get_account(primary_key: str) -> LocalAccount:
    return web3.eth.account.from_key(primary_key)


def send_n_sign_transaction(acc: LocalAccount, to: str):
    transaction = {
        "from": acc.address,
        "to": to,
        "value": 1_000_000_000_000_000_000,
        "nonce": web3.eth.get_transaction_count(acc.address),
        "gas": 200_000,
        "maxFeePerGas": 2_000_000_000,
        "maxPriorityFeePerGas": 1_000_000_000,
        "chainId": 2340,
    }
    signed = web3.eth.account.sign_transaction(transaction, "")
    tx_hash = web3.eth.send_raw_transaction(signed.rawTransaction)

    tx = web3.eth.get_transaction(tx_hash)
    logging.info(tx)
    assert tx["from"] == acc.address


def test():
    acc = get_account("")
    logging.info(f"Acc address: {acc.address}")
    # logging.info(f"Is connected: {web3.is_connected()}")
    send_n_sign_transaction(acc, null_address)


def start():
    test()
