from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

starting_page_url = 'http://secure-retreat-92358.herokuapp.com/'

# TODO Initialise the chrome driver
chrome_exe_loc = "../chromedriver.exe"
chrome_driver = webdriver.Chrome(executable_path=chrome_exe_loc)

# TODO Get the starting webpage
chrome_driver.get(url=starting_page_url)

# TODO Select the first name input
firstname_input = chrome_driver.find_element(By.NAME, 'fName')

# TODO Enter the your first name
firstname_input.send_keys('John')

# TODO Select the last name input
lastname_input = chrome_driver.find_element(By.NAME, 'lName')

# TODO Enter the your last name
lastname_input.send_keys('Doe')

# TODO Select the email input
email_input = chrome_driver.find_element(By.NAME, 'email')

# TODO Enter the your email address
email_input.send_keys('johndoe@gmail.com')

# TODO Select the 'sign up' button
signup_btn = chrome_driver.find_element(By.CSS_SELECTOR, 'form button')

# TODO Click 'sign up' button
signup_btn.click()

# TODO Press the enter key
# email_input.send_keys(Keys.ENTER)

# TODO Get the page content
heading = chrome_driver.find_element(By.CSS_SELECTOR, 'div h1')
heading_text = heading.text

par = chrome_driver.find_element(By.XPATH, '/html/body/div/p')
par_text = par.text
print(f"{heading_text} {par_text}")
