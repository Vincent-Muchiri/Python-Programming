from bs4 import BeautifulSoup
import requests
import smtplib

product_link = "https://www.amazon.com/dp/B01N9VNYJR?_encoding=UTF8&ref_=cm_sw_r_cp_ud_dp_19620KEA160JQEGC1A05&th=1"
accept_lang = "en-GB,en-US;q=0.9,en;q=0.8"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

my_email = "tripiestands@gmail.com"
password = "Virt8676!"

# TODO Get the HTML page
response = requests.get(
    url=product_link,
    headers={
        "Accept-Language": accept_lang,
        "User-Agent": user_agent
    }
)
response.raise_for_status()
product_page = response.text

# TODO Instantiate Beautifulsoup
product_soup = BeautifulSoup(product_page, "html.parser")
# print(product_soup.prettify())

# TODO Scrap the price
# prices = product_soup.find_all(name="span", class_="a-offscreen")
product_price = float(product_soup.find(name="span", class_="a-price-whole").getText().strip("."))
price_symbol = product_soup.find(name="span", class_="a-price-symbol").getText()
print(f"{price_symbol}{product_price}")

# TODO Scrap the name
# product_name = product_soup.select(selector="h1 span")
product_name = product_soup.find(name="span", id="productTitle").getText()
# print(product_name)

# TODO Check if the price is below the desired target
budget = 350
savings = budget - product_price

if product_price < budget:
    # TODO Create connection
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # with smtplib.SMTP("smtp.gmail.com", port=465) as connection:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # TODO Encrypt connection
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="vincentmuchiri1@gmail.com",
                            msg=f"Subject: Price alert testing\n\n"
                                f"The product '{product_name}' price is {product_price}, save {price_symbol}{savings}.")
        print("Email sent successfully!")
