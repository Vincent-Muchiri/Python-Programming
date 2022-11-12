from selenium import webdriver
from selenium.webdriver.common.by import By

# TODO Create a variable to hold the path of the Chrome driver
chrome_driver_path = '../chromedriver.exe'

# TODO Instantiate a browser-specific driver object
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)

# TODO Open up a webpage
product_link = "https://www.amazon.com/dp/B01N9VNYJR?_encoding=UTF8&ref_=cm_sw_r_cp_ud_dp_19620KEA160JQEGC1A05&th=1"
chrome_driver.get(url=product_link)

# TODO How to find element(s)
# chrome_driver.find_element_by_css_selector()
product_price = chrome_driver.find_element(By.CLASS_NAME, "a-price-whole")
product_name = chrome_driver.find_element(By.ID, "productTitle")
# chrome_driver.find_elements(By.TAG_NAME, '')
# chrome_driver.find_elements(By.LINK_TEXT), 'Buy Now'
# chrome_driver.find_element(By.NAME, "q")
# chrome_driver.find_element(By.CSS_SELECTOR, "")
# chrome_driver.find_element(By.XPATH, "")





# TODO Close the tab
# chrome_driver.close()

# TODO Close the entire window
chrome_driver.quit()
