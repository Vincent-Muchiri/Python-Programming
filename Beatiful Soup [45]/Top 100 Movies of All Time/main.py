import requests
from pprint import pprint
from bs4 import BeautifulSoup
import html

# TODO Get the HTML data
response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
medium_html_data = response.text

# TODO Offline data
# with open(file="data/index.html", mode="r", encoding="utf8") as html_file:
#     medium_html_data = html_file.read()

# TODO Create a BeautifulSoup object
medium_movies_soup = BeautifulSoup(medium_html_data, "html.parser")
# print(medium_movies_soup.prettify())

# TODO Inspect HTML and find sample

article_images = medium_movies_soup.select(selector="picture img")

movie_names_list = []
for image in article_images:
    image_text = html.unescape(image.get("alt"))
    movie_names_list.insert(0, image_text)

# TODO Remove the last image text
movie_names_list = movie_names_list[:-1]

with open("data/movies.txt", mode="w") as movies_txt_file:
    count = 1
    for movie in movie_names_list:
        movies_txt_file.write(f"{count} {movie}\n")
        count += 1
