# TODO Get the number of Wikipedia articles
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import mkdir, path
import pandas

page_url = "https://en.wikipedia.org/wiki/Main_Page"

# TODO Initialize a new driver
chrome_driver_dir = "../chromedriver.exe"
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_dir)

# TODO Get the url link
chrome_driver.get(url=page_url)

# TODO Get the number of articles
num_wiki_articles = chrome_driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# num_wiki_articles = chrome_driver.find_element(By.CSS_SELECTOR, '.articlecount a')
# print(num_wiki_articles.text)

# TODO Click the link to open the 'Statistics' page
num_wiki_articles.click()

# TODO Go to the page listing the most visited pages
most_viewed_pages = chrome_driver.find_element(By.LINK_TEXT, 'Most viewed pages')
most_viewed_pages.click()

# TODO Find the search bar
search = chrome_driver.find_element(By.LINK_TEXT, 'Search')

# TODO Enter 'Python' in the search bar
search.send_keys('Python')

# TODO Click the 'Enter' key on the keyboard
search.send_keys(Keys.ENTER)

# TODO Close the opened window
# chrome_driver.close()
# chrome_driver.quit()
