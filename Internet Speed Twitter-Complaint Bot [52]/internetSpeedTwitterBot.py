import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import time, sleep
from concurrent.futures import as_completed, ThreadPoolExecutor

CHROME_DRIVER_PATH = "../chromedriver.exe"
TWITTER_URL = 'https://twitter.com/login?lang=en'

class InternetSpeedTwitterBot:
    def __init__(self, promised_up:float, promised_down:float):
        self.promised_up = float(promised_up)
        self.promised_down = float(promised_down)

        # TODO Set options
        chrome_options = Options()

        # TODO Make the bot run headless i.e. without opening the browser
        chrome_options.headless = True

        # TODO Initialize the Chrome driver
        self.chrome_driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)

    def get_internet_speed(self):
        """
        This method gets the internet speeds from Fast.com
        :return: dict
        """
        fast_url = "https://fast.com/"
        print("Fetching internet speeds from fast.com...")

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
        print(f"Your upload speed is {upload_speed} {upload_units} and the download speed is {download_speed} {download_units}")

        # TODO Create a dict with the internet details
        internet_speed_details = {
            'upload_speed': upload_speed,
            'upload_units': upload_units,
            'download_speed': download_speed,
            'download_units': download_units
        }

        # print("Done")

        # TODO Return a dict
        return internet_speed_details
    def tweet_at_provider(self, internet_speed_dict: dict):
        # TODO Get the credentials
        with open("confidential.txt", mode="r") as credentials_file:
            credentials_array = credentials_file.readlines()

        username = credentials_array[0].strip("\n")
        password = credentials_array[1]

        # TODO Open new tab
        self.chrome_driver.execute_script("window.open('');")

        # TODO Switch to new tab
        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[1])

        # TODO Get the webpage
        twitter_login_page = "https://twitter.com/login?lang=en"
        self.chrome_driver.get(twitter_login_page)

        # TODO Wait for input fields to appear and be clickable
        username_input_field = WebDriverWait(self.chrome_driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, 'input')))

        # TODO Add the username to the input field
        username_input_field.send_keys(username)

        # TODO Get the next button
        next_btn = self.chrome_driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_btn.click()

        # TODO Enter the password
        sleep(5)
        # pass_input = WebDriverWait(self.chrome_driver, 30).until(EC.text_to_be_present_in_element_attribute((By.TAG_NAME, 'input'), 'name', 'password'))
        pass_input_array = [pass_input for pass_input in self.chrome_driver.find_elements(By.TAG_NAME, 'input') if pass_input.get_attribute('name') == 'password']
        pass_input_array[0].send_keys(password)

        # TODO Get the next button
        # sleep(10)
        # login_btn = WebDriverWait(self.chrome_driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'button')))
        # login_span = WebDriverWait(self.chrome_driver, 20).until(EC.text_to_be_present_in_element_attribute((By.TAG_NAME, 'div'), 'role', 'button'))
        # login_div = self.chrome_driver.find_element(By.TAG_NAME, 'button')
        login_div = self.chrome_driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')

        login_div.click()
        # login_btn.click()
        # login_span.click()
        # print("button clicked")

        # TODO Select tweet thing
        # text_ele = WebDriverWait(self.chrome_driver, '20').until(EC.text_to_be_present_in_element_attribute((By.TAG_NAME, 'br'), 'data-text', 'true'))
        # text_ele.click()
        # tweet_div = self.chrome_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        #'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]'
        # tweet_div = WebDriverWait(self.chrome_driver, 20).until(EC.element_attribute_to_include(By.TAG_NAME, 'div'), 'data-offset-key')
        # tweet_div.click()
        # tweet_div.send_keys('This is a tweet text')
        sleep(10)
        div_array = self.chrome_driver.find_elements(By.TAG_NAME, 'div')
        for div in div_array:
            if div.get_attribute('data-offset-key'):
                div.send_keys(f"Hey @internet_provider, why is my internet speed {internet_speed_dict['upload_speed']}{internet_speed_dict['upload_units']} up/ {internet_speed_dict['download_speed']}{internet_speed_dict['download_units']} down when I pay for {self.promised_up}Mbps up/ {self.promised_down}Mbps down?")

                # TODO Send the tweet
                div.send_keys(Keys.CONTROL + Keys.ENTER)
                print("Tweet sent!")
                break

        # TODO Send the tweet
        # span_array = self.chrome_driver.find_elements(By.TAG_NAME, 'div')
        # print('span array length:', len(span_array))
        # for span in span_array:
        #     try:
        #         if span.getText() == "Tweet":
        #             print(span.getText())
        #             span.click()
        #     except AttributeError:
        #         pass
        #     else:
        #         break


    def test_code(self):
        from concurrent.futures import ThreadPoolExecutor

        URL = "https://pypi.python.org/pypi/{}"

        li = ["pywp/1.3", "augploy/0.3.5"]

        def get_content(url):
            print("This is a future")
            self.chrome_driver.get(url)
            tag = self.chrome_driver.find_element(By.TAG_NAME, "a")
            # do your work here and return the result
            return tag.get_attribute("href")

        li = list(map(lambda link: URL.format(link), li))

        futures = []
        with ThreadPoolExecutor(max_workers=2) as ex:
            for link in li:
                futures.append(ex.submit(get_content, link))

        print(len(futures))
        for future in futures:
            print(future.result())