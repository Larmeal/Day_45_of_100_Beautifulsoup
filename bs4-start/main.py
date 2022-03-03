from turtle import title
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
content = response.text

soup = BeautifulSoup(content, "html.parser")
title_news = soup.find_all(name="a", class_="titlelink")
scores_news = soup.find_all(name="span", class_="score")
article_text = [con_tent.getText() for con_tent in title_news]
article_link = [con_tent.get("href") for con_tent in title_news]
article_upvote = [int(scores.getText().split()[0]) for scores in scores_news]

article_upvote_max = article_upvote.index(max(article_upvote))

artical_max = [article_text[article_upvote_max], article_link[article_upvote_max], article_upvote[article_upvote_max]]
print(artical_max)





# with open("bs4-start\website.html", encoding="utf-8") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")

# anchor_tags = soup.find_all(name="a")

# print(soup.select_one(selector="p em"))

