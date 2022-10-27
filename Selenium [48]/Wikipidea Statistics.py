# TODO Get the number of Wikipedia articles
from selenium import webdriver
from selenium.webdriver.common.by import By
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

# TODO Click the link
num_wiki_articles.click()

# TODO Get the Statistics
table_data = chrome_driver.find_elements(By.CSS_SELECTOR, 'tr td')
# print(len(table_data))

cell_names = []
cell_values = []
for cell in table_data:
    cell_data = cell.text
    if table_data.index(cell) % 2 == 0:
        cell_names.append(cell_data)
    else:
        cell_values.append(cell_data)

# print(len(cell_names), len(cell_values))

# TODO Create a stats dictionary
wiki_stats_dict = {
    'Name': cell_names,
    'Value': cell_values
}

# TODO Create a pandas dataframe
wiki_stats_dataframe = pandas.DataFrame(wiki_stats_dict)

# TODO Save the Wikipedia statistics in a csv file
if path.exists("data"):
    pass
else:
    mkdir("data")

wiki_stats_dataframe.to_csv('data/wikipidea_stats.csv', mode='w', index=True, header=True)

# TODO Close the opened window
chrome_driver.close()
chrome_driver.quit()
