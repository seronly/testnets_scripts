import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from app.driver import RABBY_EXTENSION_ID


def setup(driver: WebDriver, private_key: str, password: str) -> None:
    wait = WebDriverWait(driver, 20)

    # driver.switch_to.window(driver.window_handles[1])
    logging.info("Open Rabby")
    driver.get(f"chrome-extension://{RABBY_EXTENSION_ID}/popup.html")

    # Next btn
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))).click()
    # driver.find_element(By.XPATH, '//span[text()="Next"]').click()
    time.sleep(0.02)
    # Get start btn
    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/footer/a/button').click()
    time.sleep(0.05)

    # Import from private key btn
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]').click()
    time.sleep(0.05)
    inputs = driver.find_elements(By.XPATH, "//input")
    inputs[0].send_keys(password)
    inputs[1].send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(0.1)

    # Send private key
    driver.find_element(By.XPATH, "//input").send_keys(private_key)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div[3]/div/button').click()
    time.sleep(0.05)

    driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div[3]/div/button').click()
    logging.info("Wallet has been imported successfully")

    time.sleep(5)


def connect(driver: WebDriver) -> None:
    wait = WebDriverWait(driver, 20)

    driver.switch_to.window(driver.window_handles[-1])
    logging.info(f"Open window: {driver.title}")
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Connect"]'))
    ).click()

    logging.info("Wallet has been connected!")


def sign_message(driver: WebDriver) -> None:
    wait = WebDriverWait(driver, 20)

    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(By.XPATH, '//span[text()="Sign and Create"]').click()
    time.sleep(0.02)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Confirm"]'))
    ).click()
    logging.info("Message has been signed!")


def network_approve(driver: WebDriver) -> None:
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.find_element(By.XPATH, '//span[text()="Add"]').click()
