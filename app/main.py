import time

from eth_account.signers.local import LocalAccount
import hashlib

from . import mm

from .db import get_wallet, init_db
from .models import Client, Wallet


import logging

logger = logging.getLogger("web3.HTTPProvider")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
)

null_address = "0x0000000000000000000000000000000000000000"


def start():
    global driver
    driver = mm.launchSeleniumWebdriver()
    driver.get("https://app-olympia.atleta.network/faucet")
    tw = get_wallet(id=10)
    mm.metamaskSetup("sad adasd asdasd asdasd", "admin")

    time.sleep(1000)
    driver.quit()
    # time_now = int(time.time())
    # kecc = Client.web3.keccak(text=str(time_now))
    # hex_number = hashlib.sha256(str(time_now).encode()).hexdigest()
    # message = f"Welcome to the Atleta Olympia. Sign this message to complete login!\n{hex_number[2:18]}"
    # tw = Client.get_wallet_from_private_key(
    #     "0x4c2b4816bc15afb7db3ba33abc42fa2004c320a3f07564f97e8466ae83d7fc12"
    # )

    # project id ee1a8c4bc65db61f4c6062984c37bfa2
    #  GET https://app-olympia.atleta.network/api/pub/faucet?account_id=0xDb86c42a85028Bd8B2b20B9A7065dF8441Eb1f98
    # faucet.FundsSent
    # https://web2-testnet-api.atleta.network/pub/auth/login
