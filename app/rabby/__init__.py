import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from app.driver import RABBY_EXTENSION_ID


def rabby_setup(driver: WebDriver, private_key: str, password: str):

    driver.switch_to.window(driver.window_handles[0])
    driver.get("chrome-extension://{}/popup.html".format(RABBY_EXTENSION_ID))
    time.sleep(2)
    # Next btn
    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/footer/button').click()
    time.sleep(2)
    # Get start btn
    driver.find_element(By.XPATH, '//*[@id="root"]/div/section/footer/a/button').click()
    time.sleep(2)
    # Import from private key btn
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]').click()
    time.sleep(2)
    inputs = driver.find_elements(By.XPATH, "//input")
    inputs[0].send_keys(password)
    inputs[1].send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)
    # Send private key
    driver.find_element(By.XPATH, "//input").send_keys(private_key)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div[3]/div/button').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/form/div[3]/div/button').click()
    print("Wallet has been imported successfully")

    time.sleep(5)
