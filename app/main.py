import time

from eth_account.signers.local import LocalAccount

from app.wallets import rabby

from .driver import launch_selenium_webdriver
from .db import get_wallet, init_db
from .models import Client, Wallet
from .projects import atleta

import logging

logger = logging.getLogger("web3.HTTPProvider")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)

null_address = "0x0000000000000000000000000000000000000000"


def start():
    driver = launch_selenium_webdriver()
    tw_row = get_wallet(id=10)
    rabby.setup(driver=driver, private_key=tw_row[2], password="qwerty123123")
    atleta.claim_faucet(driver)
    time.sleep(1000)
    driver.quit()

    # project id ee1a8c4bc65db61f4c6062984c37bfa2
    #  GET https://app-olympia.atleta.network/api/pub/faucet?account_id=0xDb86c42a85028Bd8B2b20B9A7065dF8441Eb1f98
    # faucet.FundsSent
    # https://web2-testnet-api.atleta.network/pub/auth/login
