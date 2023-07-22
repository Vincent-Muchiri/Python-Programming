from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

import requests
from pprint import pprint

address_array = ['address1', 'address2', 'address3', 'address4']
rental_price_array = ['price1', 'price2', 'price3', 'price4']
link_array = ['link1', 'link2', 'link3', 'link4']

# TODO Create webdriver options
driver_options = Options()

# TODO Set headless option to True or False
driver_options.headless = False

# TODO Instantiate webdriver
chrome_driver = webdriver.Chrome(executable_path="../chromedriver.exe", options=driver_options)

# TODO Open the form online
chrome_driver.get(url="https://forms.gle/GaCAMYw9tTpeudYK7")



for property_index in range(len(address_array)):
    # TODO Get all the inputs element objects
    all_input_elems_array = chrome_driver.find_elements(By.TAG_NAME, 'input')
    # print(input_elems)
    input_elems_array = []
    for input_elem in all_input_elems_array:
        if input_elem.get_attribute('type') == "text":
            input_elems_array.append(input_elem)

    address = address_array[property_index]
    rental_price = rental_price_array[property_index]
    link = link_array[property_index]

    print(property_index)
    print(input_elems_array[0])
    input_elems_array[0].send_keys(address)
    input_elems_array[1].send_keys(rental_price)
    input_elems_array[2].send_keys(link)


    # TODO Click submit button
    submit_btn = chrome_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_btn.click()

    # TODO Click the link to a new response
    new_response_btn = WebDriverWait(chrome_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    new_response_btn.click()

    # sleep(5)