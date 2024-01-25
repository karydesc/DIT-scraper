import time

import requests
from bs4 import BeautifulSoup
from lxml import html
import os





f = open("id.txt", "r")
webid = int(f.read())
f.close()

URL = "https://www.dit.uoi.gr/news.php?sa=view_new&id=" + str(webid)

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
get404 = soup.find("h1")
status = get404.getText() == "Η σελίδα δεν βρέθηκε"

if status:
    time.sleep(5)
    os.system("python3 main.py")


webid += 1
f = open("id.txt", "w")
f.write(str(webid))
f.close()


body = soup.find("div", class_="chris")
title = soup.find("h1", class_="title")
subtitle = soup.find("h2", class_="subtitle")
category_element = soup.find('b', string='Κατηγορία:')
category_text = category_element.find_next_sibling(string=True).strip()



