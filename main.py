import time

import requests
from bs4 import BeautifulSoup


def check404(url_check):
    temp_page = requests.get(url_check)
    temp_soup = BeautifulSoup(temp_page.content, "html.parser")
    get404 = temp_soup.find("h1")
    return get404.getText() == "Η σελίδα δεν βρέθηκε"


f = open("id.txt", "r")
webid = int(f.read())
f.close()
URL = "https://www.dit.uoi.gr/news.php?sa=view_new&id=" + str(webid)
while check404(URL):
    time.sleep(5)
    print("not found")
print("found")
webid += 1
f = open("id.txt", "w")
f.write(str(webid))
f.close()

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

body = soup.find("div", class_="chris")
title = soup.find("h1", class_="title")
subtitle = soup.find("h2", class_="subtitle")
category_element = soup.find('b', string='Κατηγορία:')
category_text = category_element.find_next_sibling(string=True).strip()

print(" Category: ", category_text, "\n", "Title: " + title.getText(), '\n', "Subtitle: ", subtitle, "\n",body.getText(), '\n')

token = "EAAM0b8NuPY0BO2BpbI9CxHKQODWB08PlD9KrXtwqHQvqADougldhafWKYDi9DiZAkncd1FKoeSYHEzgEYydbC8SwsE2ukPH06V8Wwx1licbmThVI5Jc21tieeP5ozZAySGya7aN2gGE05EQX7Ypb9vEFZCCmYVksCmJzBN6FLQWena347ppuY0K"


