from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import time, sleep

webpage_url = 'https://orteil.dashnet.org/cookieclicker/'

# TODO Initialize the webdriver
chrome_exe_dir = '../chromedriver.exe'
chrome_driver = webdriver.Chrome(executable_path=chrome_exe_dir)

# TODO Get the link
chrome_driver.get(url=webpage_url)

# TODO Delay so that the page can load
print("Waiting for page to load")
still_waiting = True
secs_remaining = 15
while still_waiting:
    print(f"{secs_remaining} seconds remaining")
    sleep(1)
    secs_remaining -= 1
    if secs_remaining < 0:
        still_waiting = False

# TODO Select the language
lang_btn = chrome_driver.find_element(By.ID, 'langSelect-EN')
lang_btn.click()

# TODO Delay so that the page can load
print("Waiting for page to load")
secs_remaining = 5
still_waiting = True
while still_waiting:
    print(f"{secs_remaining} seconds remaining")
    sleep(1)
    secs_remaining -= 1
    if secs_remaining < 0:
        still_waiting = False

# TODO Get the cookie element
# cookie = chrome_driver.find_element(By.ID, 'bigCookie')

next_product_num = 0
start_time = time()

# next_product_price = int(chrome_driver.find_element(By.CSS_SELECTOR, f"#productPrice{next_product}").text.replace(",", ""))
# cookies_earned = int(chrome_driver.find_element(By.CSS_SELECTOR, f"#cookies").text.split()[0].replace(",", ""))
# earning_rate = float(chrome_driver.find_element(By.CSS_SELECTOR, f"#cookiesPerSecond").text.split(": ")[-1])
# print(next_product_price, cookies_earned, earning_rate)
#
# time_needed = (next_product_price - cookies_earned) / earning_rate
time_needed = 10
# print(f"The initial time needed is: {time_needed},\n"
#       f"the next product price is: {next_product_price},\n"
#       f"the cookies earned initially are: {cookies_earned},\n"
#       f"the initial earning rate is: {earning_rate}")
print("")

while True:
    # TODO Get the cookie element
    cookie = chrome_driver.find_element(By.ID, 'bigCookie')

    # TODO Select the cookie
    cookie.click()

    time_elapsed = time() - start_time
    # print(time_elapsed)

    if time_elapsed >= time_needed:
        # TODO Buy the product
        next_product_elem = chrome_driver.find_element(By.CSS_SELECTOR, f"#product{next_product_num}")

        # TODO Check if the the price is enabled
        class_name = next_product_elem.get_attribute("class")
        # print(class_name)
        if "enabled" in class_name:
            next_product_elem.click()

            # Set the next product
            next_product_num += 1

            next_product_price = int(chrome_driver.find_element(By.CSS_SELECTOR, f"#productPrice{next_product_num}").text.replace(",", ""))
            cookies_earned = int(chrome_driver.find_element(By.CSS_SELECTOR, f"#cookies").text.split()[0].replace(",", ""))
            print(chrome_driver.find_element(By.CSS_SELECTOR, f"#cookiesPerSecond").text.split(": ")[-1])
            earning_rate = float(chrome_driver.find_element(By.CSS_SELECTOR, f"#cookiesPerSecond").text.split(": ")[-1])

            time_needed = (next_product_price - cookies_earned) / earning_rate

            # TODO Reset time
            start_time = time()

            print(f"The time needed is: {time_needed},\n"
                  f"the next product price is: {next_product_price},\n"
                  f"the cookies earned initially are: {cookies_earned},\n"
                  f"the initial earning rate is: {earning_rate}")
            print("")

    # else:
    #     # cookies_earned = int(cookie_clicker_soup.select_one(selector=f"#cookies").text)
    #     # earning_rate = int(cookie_clicker_soup.select_one(selector=f"#cookiesPerSecond").text)
    #     #
    #     # time_needed = (next_product_price - cookies_earned) / earning_rate
    #     time_needed = 30
    #     start_time = time()

# If there's enough cookie to buy a product, the product becomes enabled. To check this, we can either
# 1. Loop through the product divs class name if it has changed from 'disabled' to 'enabled'
# 2. Create a list of dicts with the divs and their price and compare that to the current number of cookies with id name 'cookies'
# Logic:
# 1. Get the price of the next product
# 2. Get the cookies/sec
# 3. Calculate the number of seconds needed to earn the cookies
# 4. Start the clock and when it reaches that time it should check if the product is enabled
# 5. If it isn't yet still available, check the difference and calculate the time needed and restart the clock


