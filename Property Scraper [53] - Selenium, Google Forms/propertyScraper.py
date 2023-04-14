from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
from pprint import pprint


class PropertyScraper:
    def __init__(self):
        self.FORM_URL = "https://forms.gle/GaCAMYw9tTpeudYK7"
        self.PROPERTY_PAGE_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

        # TODO Create webdriver options
        driver_options = Options()

        # TODO Set headless option to True or False
        driver_options.headless = True

        # TODO Instantiate webdriver
        chrome_driver = webdriver.Chrome(executable_path="../chromedriver.exe", options=driver_options)


    def get_property_data(self):
        # TODO Get the page html
        response = requests.get(self.PROPERTY_PAGE_URL)
        response.raise_for_status()
        property_page_html = response.text
        pprint(property_page_html)


        # TODO Instantiate BeautifulSoup
        zillow_soup = BeautifulSoup(property_page_html, parser="html.parser")

        # TODO Get the property indices
        address_array = zillow_soup.find_all(name='address')
        print(len(address_array))


    def fill_property_data(self):
        pass

    def form_to_excel(self):
        pass