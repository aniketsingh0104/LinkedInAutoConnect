# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from contants import DEFAULT_DRIVER_WAIT, LINKEDIN_INVITATION_MANAGER_URL, SCROLL_PAUSE_TIME, \
    XPATH_PATTERN_OF_LINKEDIN_CONNECTION_ACCEPT_BUTTON, EXPLICIT_WAIT_FOR_SIGN_IN


def _prepare_driver(chrome_driver_path: str):
    # create new chrom driver
    chrome_driver = webdriver.Chrome(chrome_driver_path)

    # selenium will wait for 30 secs before throwing an exception
    chrome_driver.implicitly_wait(DEFAULT_DRIVER_WAIT)

    chrome_driver.maximize_window()

    return chrome_driver


def main(chrome_driver_path: str):
    driver = _prepare_driver(chrome_driver_path)

    try:
        driver.get(LINKEDIN_INVITATION_MANAGER_URL)

        # wait for sign in to happen -> time in seconds
        wait = WebDriverWait(driver, EXPLICIT_WAIT_FOR_SIGN_IN)

        wait.until(
            EC.presence_of_element_located((By.XPATH, XPATH_PATTERN_OF_LINKEDIN_CONNECTION_ACCEPT_BUTTON)))

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # wait for the page to load
            time.sleep(SCROLL_PAUSE_TIME)

            # Wait till element becomes clickable
            WebDriverWait(driver, SCROLL_PAUSE_TIME).until(
                EC.element_to_be_clickable((By.XPATH,
                                            XPATH_PATTERN_OF_LINKEDIN_CONNECTION_ACCEPT_BUTTON)))

            # find all accept buttons
            all_accept_buttons = driver.find_elements(By.XPATH, XPATH_PATTERN_OF_LINKEDIN_CONNECTION_ACCEPT_BUTTON)

            for button in all_accept_buttons:
                # click all on buttons
                button.send_keys(Keys.RETURN)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            # check if no other request is pending
            if new_height == last_height:
                break

            last_height = new_height

    finally:
        driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    driver_path = "<ENTER_YOUR_CHROMIUM_WEBDRIVER_PATH>"

    if driver_path == "<ENTER_YOUR_CHROMIUM_WEBDRIVER_PATH>":
        raise ValueError("Please enter the correct path of your webdriver")

    main(driver_path)

