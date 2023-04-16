from pprint import pprint

from propertyScraper import PropertyScraper

# TODO Initiate the class
property_scraper_bot = PropertyScraper()

# TODO Scrap the property data and store it in a dict
scraped_data_dict = property_scraper_bot.get_property_data()
print(scraped_data_dict)

# TODO Fill in the Google sheet form using Selenium
property_scraper_bot.fill_property_data(scraped_data_dict)

# TODO View the data in an excel file
property_scraper_bot.form_to_excel()