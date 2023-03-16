import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import time, sleep
from concurrent.futures import as_completed, ThreadPoolExecutor

CHROME_DRIVER_PATH = "../chromedriver.exe"
TWITTER_URL = 'https://twitter.com/login?lang=en'

class InternetSpeedTwitterBot:
    def __init__(self):
        self.promised_up = 10
        self.promised_down = 150

        # TODO Initialize the Chrome driver
        self.chrome_driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def get_internet_speed(self):
        """
        This method gets the internet speeds from Fast.com
        :return: dict
        """
        fast_url = "https://fast.com/"

        # TODO Get the initial website page
        self.chrome_driver.get(fast_url)

        # TODO Wait for download speeds to be complete
        show_more_info_btn = WebDriverWait(self.chrome_driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Show more info")))

        # TODO Get the download speed and units
        download_speed = float(self.chrome_driver.find_element(By.ID, "speed-value").text)
        download_units = self.chrome_driver.find_element(By.ID, "speed-units").text

        # print(download_speed, download_units)

        # TODO Click the link button
        show_more_info_btn.click()

        # TODO Wait for the upload speed test to be complete
        WebDriverWait(self.chrome_driver, 60).until(EC.text_to_be_present_in_element_attribute((By.ID, 'speed-progress-indicator'), 'class', 'succeeded'))

        # TODO Get the upload speeds and units
        upload_speed = float(self.chrome_driver.find_element(By.ID, 'upload-value').text)
        upload_units = self.chrome_driver.find_element(By.ID, 'upload-units').text

        # print(upload_speed, upload_units)
        print(f"The upload speed is {upload_speed} {upload_units} and the download speed is {download_speed} {download_units}")

        # TODO Create a dict with the internet details
        internet_speed_details = {
            'upload_speed': upload_speed,
            'upload_units': upload_units,
            'download_speed': download_speed,
            'download_units': download_units
        }

        # TODO Return the a dict
        return internet_speed_details
    def tweet_at_provider(self):
        pass
