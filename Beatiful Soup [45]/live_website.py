import requests
from bs4 import BeautifulSoup
from pprint import pprint

# TODO Get the html code
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
y_comb_html = response.text

# TODO For offline testing
# with open("data/y-comb-news.html", encoding="utf8") as html_file:
#     y_comb_html = html_file.read()

# span class = "titleline"
y_comb_soup = BeautifulSoup(y_comb_html, "html.parser")
# print(y_comb_soup.prettify())

# TODO Get all the news span
news_span_list = y_comb_soup.find_all(name="span", class_="titleline")

news_titles = []
news_links = []
# TODO Get the news link and news title
for news_span in news_span_list:
    news_title = news_span.getText()
    news_titles.append(news_title)
    # print(news_title)
    news_link = news_span.select_one(selector="a").get("href")
    # print(news_link)
    news_links.append(news_link)

# TODO Get the each table data
score_rows = y_comb_soup.find_all(name="td", class_="subtext")

# TODO Get the upvote values and assign 0 to where they don't exist(ads)
score_list = []
for row in score_rows:
    score_span = row.find(name="span", class_="score")
    if not score_span:
        score = 0
    else:
        score = int(score_span.getText().split()[0])

    score_list.append(score)

print(score_list)

popular_score = max(score_list)
popular_score_index = score_list.index(popular_score)
popular_news_title = news_titles[popular_score_index]
popular_news_link = news_links[popular_score_index]
print(f"News title: {popular_news_title}\nNews link: {popular_news_link}\nNo. of upvotes: {popular_score}")

