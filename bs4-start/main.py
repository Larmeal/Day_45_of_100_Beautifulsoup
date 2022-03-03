from bs4 import BeautifulSoup

with open("bs4-start\website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

anchor_tags = soup.find_all(name="a")

for tag in anchor_tags:
    print(tag.getText())

print(anchor_tags[0].getText())

