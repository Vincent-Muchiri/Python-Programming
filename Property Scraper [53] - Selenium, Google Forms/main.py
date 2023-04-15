from pprint import pprint

from propertyScraper import PropertyScraper

# TODO Initiate the class
property_scraper_bot = PropertyScraper()

# TODO Scrap the property data and store it in a dict
scraped_property_details_dict = property_scraper_bot.get_property_data()
