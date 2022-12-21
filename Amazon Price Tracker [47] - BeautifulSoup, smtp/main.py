from bs4 import BeautifulSoup
import requests
import smtplib

# PRODUCT_LINK = "https://www.amazon.com/dp/B01N9VNYJR?_encoding=UTF8&ref_=cm_sw_r_cp_ud_dp_19620KEA160JQEGC1A05&th=1"
# PRODUCT_LINK = "https://www.amazon.com/Eastar-Student-Saxophone-Carrying-Mouthpiece/dp/B07HL8YNJH/ref=zg_bs_11972111_sccl_2/133-0211481-6308405?psc=1"
PRODUCT_LINK = "https://www.amazon.com/dp/B09LQS9N9X/?coliid=I20M5FZ5B47L5Z&colid=2DKWDVE59FPIH&psc=1&ref_=lv_ov_lig_dp_it"
ACCEPT_LANG = "en-GB,en-US;q=0.9,en;q=0.8"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

MY_EMAIL = "appdevemail.test@gmail.com"
APP_PASSWORD = "hthxjiusuwxxvszy"

# TODO Get the HTML page
response = requests.get(
    url=PRODUCT_LINK,
    headers={
        "Accept-Language": ACCEPT_LANG,
        "User-Agent": USER_AGENT
    }
)
response.raise_for_status()
product_page_html = response.text

# TODO Save the data locally
with open("data/product_page.html", mode="w", encoding="utf8") as product_html_file:
    product_html_file.write(product_page_html)

# TODO Instantiate Beautifulsoup
product_soup = BeautifulSoup(product_page_html, "html.parser")
# print(product_soup.prettify())

# TODO Scrap the price
# price_symbol = product_soup.find_all(name="span", class_="a-price-symbol")
# print(price_symbol)
span_content = product_soup.find_all(name="span", class_="a-offscreen")
# print(span_content)
# print(product_soup.find_all(name="span", class_="a-offscreen"))
for content in span_content:
    text = content.getText()
    if "$" in text:
        price_symbol = "$"
        product_price = float(text.strip("$"))
        print(product_price)
# print(product_soup.find_all(name="span", class_="a-price-whole"))
# product_price = float(product_soup.find(name="span", class_="a-price-whole").getText().strip("."))
# price_symbol = product_soup.find(name="span", class_="a-price-symbol").getText()
# print(f"{price_symbol}{product_price}")

# TODO Scrap the name
# product_name = product_soup.select(selector="h1 span")
product_name = product_soup.find(name="span", id="productTitle").getText()
print(product_name)

# TODO Check if the price is below the desired target
budget = 600

if product_price < budget:
    savings = budget - product_price
    print(savings)
    # TODO Create connection
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # with smtplib.SMTP("smtp.gmail.com", port=465) as connection:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # TODO Encrypt connection
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="appdevemail.test@yahoo.com",
                            msg=f"Subject: Price alert testing\n\n"
                                f"The product '{product_name}' price is {product_price}, save {price_symbol}{savings}.")
        print("Email sent successfully!")

