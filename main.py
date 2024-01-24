import requests
from bs4 import BeautifulSoup
from lxml import html
URL = "https://www.dit.uoi.gr/news.php?sa=view_new&id=8733"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
body = soup.find("div", class_="chris")

title = soup.find("h1", class_="title")
subtitle = soup.find("h2", class_="subtitle")
category_element = soup.find('b', string='Κατηγορία:')
if category_element:
    # Get the next sibling, which contains the desired text
    category_text = category_element.find_next_sibling(string=True).strip()


print(" Category: ", category_text, "\n", "Title: " + title.getText(), '\n', "Subtitle: ", subtitle, "\n", body.getText(), '\n')

