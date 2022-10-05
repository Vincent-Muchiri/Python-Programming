from bs4 import BeautifulSoup
import lxml
from pprint import pprint

# TODO Open the html file, add encoding type incase of error and read the file
with open("website.html", encoding="utf8") as html_file:
    contents = html_file.read()

# TODO Create a BeautifulSoup object and pass the content and parser(html or lxml)
soup = BeautifulSoup(contents, "html.parser")

# TODO Print the html content
# print(soup)                 # Prints an unstructured html
# print(soup.prettify())      # Prints structured html

# TODO Get the tags and content inside the first tags
# print(soup.title)           # Prints <title> and whatever is in it
# print(soup.title.string)    # Prints the contents inside the <title>
# print(soup.a)               # Prints the first <a>

# TODO Get all tags and the content
all_anchor_tags = soup.find_all(name="a")   # Returns a list of all anchor tags

# TODO Get the contents of anchor tags
for anchor_tag in all_anchor_tags:
    print(anchor_tag)
    # print(anchor_tag.getText)         # Prints the text and href
    # print(anchor_tag.string)          # Prints the text only
    print(anchor_tag.get("href"))     # Prints the href only
    pass

# TODO Search by attribute
heading = soup.find(name="h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# TODO Search using selector
company_url = soup.select_one(selector="p a")  # Get an anchor tag that sits inside a paragraph
name = soup.select_one(selector="#name")    # Get a tag with id= name
soup.select(selector=".heading")    # Get all with class=heading

