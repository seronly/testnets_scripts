import logging
from time import sleep
import requests
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from app.wallets import rabby


def claim_faucet(driver: WebDriver):
    driver.get("https://app-olympia.atleta.network/faucet")

    connect_btn = driver.find_element(By.XPATH, '//button[text()="Connect"]')

    if connect_btn:
        connect_wallet(driver)

    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//button[text()="Send me $ATLA"]').click()
    logging.info("Tokens has been claimed!")
    # wait.until(
    #     EC.element_to_be_clickable((By.XPATH, '//button[text()="Send me $ATLA"]'))
    # ).click()


def connect_wallet(driver: WebDriver):
    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Connect"]'))
    ).click()
    sleep(2)
    # Select RabbyWallet
    driver.execute_script(
        """
        document.querySelector("body > w3m-modal").shadowRoot.querySelector("wui-flex > wui-card > w3m-router").shadowRoot.querySelector("div > w3m-connect-view").shadowRoot.querySelector("wui-flex > w3m-wallet-login-list").shadowRoot.querySelector("wui-flex > w3m-connect-injected-widget").shadowRoot.querySelector("wui-flex > wui-list-wallet[name='Rabby Wallet']").shadowRoot.querySelector('button').click();
        """
    )
    sleep(2)
    rabby.connect(driver)
    sleep(1)
    rabby.sign_message(driver)
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script(
        """
document.querySelector("body > w3m-modal").shadowRoot.querySelector("wui-flex > wui-card > w3m-router").shadowRoot.querySelector("div > w3m-unsupported-chain-view").shadowRoot.querySelector("wui-flex > wui-flex:nth-child(2) > wui-list-network[name='Atleta Olympia']").shadowRoot.querySelector("button").click();
        """
    )
    sleep(1)
    rabby.network_approve(driver)


def connect_by_request(driver: WebDriver):
    # cookies = driver.get_cookies()
    # session = requests.Session()
    # for cookie in cookies:
    #     session.cookies.set(cookie["name"], cookie["value"])
    # res = session.get(
    #     "https://rpc.walletconnect.com/v1/profile/reverse/0xcD9D83A5A3fD5e12659619734b380c03323ad521?projectId=ee1a8c4bc65db61f4c6062984c37bfa2"
    # )
    pass


def create_porposal():
    pass


def stake(driver: WebDriver):
    pass
