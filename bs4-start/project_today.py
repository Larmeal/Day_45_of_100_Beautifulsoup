from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
source = response.text

soup = BeautifulSoup(source, "html.parser")

movies_tag = [tag.getText() for tag in soup.find_all(name="h3", class_="title")][::-1]

with open("bs4-start\list_movie.txt", "a", encoding="utf-8") as file:
    for movie in movies_tag:
        file.write(str(movie) + "\n")
        
