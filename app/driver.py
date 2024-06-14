import os
import platform
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


# METAMASK_EXTENSION_PATH = os.getcwd() + "\\app\mm\metamaskExt.crx"
METAMASK_EXTENSION_PATH = os.getcwd() + "/app/wallets/mm/metamaskExt.crx"
METAMASK_EXTENSION_ID = "nkbihfbeogaeaoehlefnkodbefgpgknn"

RABBY_EXTENSION_ID = "acmacodkjbdgmoleebolmdjonilkdbch"
RABBY_EXTENSION_PATH = os.getcwd() + "/app/wallets/rabby/rabby.crx"


def get_chromedriver_path():
    os_name = platform.system()
    if os_name == "Windows":
        return os.getcwd() + "\\webdrivers\chromedriver.exe"
    elif os_name == "Linux":
        return os.getcwd() + "/webdrivers/chromedriver_linux"
    elif os_name == "Darwin":
        return os.getcwd() + "/webdrivers/chromedriver_macos"
    else:
        raise Exception(f"Unsupported operating system: {os_name}")


def get_options() -> Options:
    print("path", RABBY_EXTENSION_PATH)
    chrome_options = Options()
    chrome_options.add_extension(RABBY_EXTENSION_PATH)
    chrome_options.add_argument("--lang=en")
    # chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    return chrome_options


def launch_selenium_webdriver() -> WebDriver:
    chrome_options = get_options()
    chrome_service = Service(executable_path=get_chromedriver_path())

    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    time.sleep(5)
    print("Extension has been loaded")
    return driver
