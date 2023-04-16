from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
from pprint import pprint


class PropertyScraper:
    def __init__(self):
        self.FORM_URL = "https://forms.gle/GaCAMYw9tTpeudYK7"
        self.PROPERTY_PAGE_URL = "https://www.property24.co.ke/1-bedroom-apartments-flats-to-rent-in-nairobi-c1890?toprice=20000"


    def get_property_data(self):
        '''
        Scraps property data and returns the data as a dict
        :return: dict: property details
        '''

        # TODO Get the page html
        response = requests.get(self.PROPERTY_PAGE_URL)
        response.raise_for_status()
        property_page_html = response.text
        # pprint(property_page_html)

        # TODO Instantiate BeautifulSoup
        property24_soup = BeautifulSoup(property_page_html, features="html.parser")

        # TODO Get the rental prices
        # price_div = property24_soup.find(name='div', class_='sc_listingTilePrice')
        # price_child_nodes_array = price_div.findChildren()
        # for child in price_child_nodes_array:
        #     print(child.text.replace("\r\n",""))

        price_div_array = property24_soup.find_all(name='div', class_='sc_listingTilePrice')

        rental_price_array = []
        for price_div in price_div_array:
            # x.append(price_div.text.strip().replace('\n\r\n', '').replace('\r\n', '').replace(" ", ""))
            rental_price_array.append(" ".join(price_div.text.split()))

        # TODO Get the property address
        address_div_array = property24_soup.find_all(name='div', class_='sc_listingTileAddress')
        address_array = []
        for address_div in address_div_array:
            address_array.append(" ".join(address_div.text.split()))

        # TODO Get the property link
        link_tag_array = property24_soup.find_all(name='a', class_='title', attrs='href')
        link_array = []
        for link_tag in link_tag_array:
            link_array.append(f"https://www.property24.co.ke{link_tag.get('href')}")

        # print(len(rental_price_array))
        # print(len(address_array))
        # print(len(link_array))

        scraped_property_details_dict = {
            'address': address_array,
            'rental price': rental_price_array,
            'link': link_array
        }

        return scraped_property_details_dict

    def fill_property_data(self, property_data: dict):
        # TODO Create webdriver options
        driver_options = Options()

        # TODO Set headless option to True or False
        driver_options.headless = False

        # TODO Instantiate webdriver
        chrome_driver = webdriver.Chrome(executable_path="../chromedriver.exe", options=driver_options)

        # TODO Open the form online
        chrome_driver.get(url=self.FORM_URL)

        # TODO Get all the inputs element objects
        all_input_elems_array = chrome_driver.find_elements(By.TAG_NAME, 'input')
        # print(input_elems)
        input_elems_array = []
        for input_elem in all_input_elems_array:
            if input_elem.get_attribute('type') == "text":
                input_elems_array.append(input_elem)

        address_array = property_data['address']
        rental_price_array = property_data['rental price']
        link_array = property_data['link']

        # TODO Enter the data to the form
        for property_index in range(len(address_array)):
            # TODO Get all the inputs element objects
            all_input_elems_array = chrome_driver.find_elements(By.TAG_NAME, 'input')
            # print(input_elems)
            input_elems_array = []
            for input_elem in all_input_elems_array:
                if input_elem.get_attribute('type') == "text":
                    input_elems_array.append(input_elem)

            input_elems_array[0].send_keys(address_array[property_index])
            input_elems_array[1].send_keys(rental_price_array[property_index])
            input_elems_array[2].send_keys(link_array[property_index])

            # TODO Click submit button
            submit_btn = chrome_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit_btn.click()

            # TODO Click the link to a new response
            new_response_btn = WebDriverWait(chrome_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
            new_response_btn.click()




    def form_to_excel(self):
        pass