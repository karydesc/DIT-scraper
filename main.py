import time

import requests
from bs4 import BeautifulSoup


def check404(url_check):
    temp_page = requests.get(url_check)
    temp_soup = BeautifulSoup(temp_page.content, "html.parser")
    get404 = temp_soup.find("h1")
    return get404.getText() == "Η σελίδα δεν βρέθηκε"

def writeNewID(web_id):
    f = open("id.txt", "w")
    f.write(str(web_id))
    f.close()


f = open("id.txt", "r")
webid = int(f.read())
f.close()


while True:
    URL = "https://www.dit.uoi.gr/news.php?sa=view_new&id=" + str(webid)
    if not check404(URL):
        print("found at "+str(webid))
        webid += 1
        writeNewID(webid) #write to file the incremented id for which the loop will continue searching
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        body = soup.find("div", class_="chris")
        title = soup.find("h1", class_="title")
        subtitle = soup.find("h2", class_="subtitle")
        category_element = soup.find('b', string='Κατηγορία:')
        category_text = category_element.find_next_sibling(string=True).strip()

        print(" Category: ", category_text, "\n", "Title: " + title.getText(), '\n', "Subtitle: ", subtitle, "\n",
              body.getText(), '\n')
        continue

    print("not found")
    time.sleep(5)




page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

body = soup.find("div", class_="chris")
title = soup.find("h1", class_="title")
subtitle = soup.find("h2", class_="subtitle")
category_element = soup.find('b', string='Κατηγορία:')
category_text = category_element.find_next_sibling(string=True).strip()

print(" Category: ", category_text, "\n", "Title: " + title.getText(), '\n', "Subtitle: ", subtitle, "\n",body.getText(), '\n')

token = "EAAM0b8NuPY0BO2BpbI9CxHKQODWB08PlD9KrXtwqHQvqADougldhafWKYDi9DiZAkncd1FKoeSYHEzgEYydbC8SwsE2ukPH06V8Wwx1licbmThVI5Jc21tieeP5ozZAySGya7aN2gGE05EQX7Ypb9vEFZCCmYVksCmJzBN6FLQWena347ppuY0K"


