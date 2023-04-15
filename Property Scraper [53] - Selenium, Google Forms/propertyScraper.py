from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
from pprint import pprint


class PropertyScraper:
    def __init__(self):
        self.FORM_URL = "https://forms.gle/GaCAMYw9tTpeudYK7"
        self.PROPERTY_PAGE_URL = "https://www.property24.co.ke/1-bedroom-apartments-flats-to-rent-in-nairobi-c1890?toprice=20000"

        # TODO Create webdriver options
        driver_options = Options()

        # TODO Set headless option to True or False
        driver_options.headless = True

        # TODO Instantiate webdriver
        chrome_driver = webdriver.Chrome(executable_path="../chromedriver.exe", options=driver_options)


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


    def fill_property_data(self):
        pass

    def form_to_excel(self):
        pass