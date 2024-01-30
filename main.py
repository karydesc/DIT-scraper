import time
import requests
from bs4 import BeautifulSoup


def formURL(num):
    return "https://www.dit.uoi.gr/news.php?sa=view_new&id=" + str(num)


def checkForLinks():
    elements = soup.select('a[rel="noopener"]')
    if not elements:
        return
    for element in elements:
        link = element['href']
        if link.startswith("/files"):
            link = "dit.uoi.gr" + link
        plain_text_link = f"{element.text}: {link}"
        element.replace_with(plain_text_link)


def getBody(obj):
    return obj.find("div", class_="chris").getText()


def getTitle(obj):
    temp = obj.find("h1", class_="title")
    return temp.getText()


def getSubtitle(obj):
    temp = obj.find("h2", class_="subtitle")
    return temp.getText()


def getCategory(obj):
    category_element = obj.find('b', string='Κατηγορία:')
    temp = category_element.find_next_sibling(string=True).strip()
    return temp


def postToFB(cat, title_, body_):
    if cat == "Διάλεξη" or cat == "Μάθημα":
        image_path = "./img/lesson_announce.jpg"
    elif cat == "Γραμματείας / Τμήμα" or cat == "Γραμματείας / Τμήμα, Πρωτοετείς" or cat == "Μεταπτυχιακό Πρόγραμμα Σπουδών" or cat == "Εκδηλώσεις":
        image_path = "./img/announce_from_tmhma.jpg"
    elif cat == "Σημαντικά":
        image_path = "./img/important_announce.jpg"
    elif cat == "Εργαστήριο":
        image_path = "./img/lab_announce.jpg"
    elif cat == "Erasmus" or cat == "Λοιπές Ανακοινώσεις":
        image_path = "./img/general_announce.jpg"
    else:
        image_path = "invalid"

    post_url = 'https://graph.facebook.com/{}/photos'.format(dst_id)
    file = {"source": open(image_path, 'rb')}
    payload = {
        "access_token": access_token,
        "message": title_ + "\n\n\n\n" + body_,
    }
    r = requests.post(post_url, data=payload, files=file)
    print(r.text)


access_token = ""
dst_id = ""


def check404(url_check):  # returns true if site doesnt exist
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
    URL = formURL(webid)
    if not check404(URL):  # if site exists
        print("found at " + str(webid))
        webid += 1
        writeNewID(webid)  # write to file the incremented id for which the loop will continue searching
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        checkForLinks()

        body = getBody(soup)
        title = getTitle(soup)
        category = getCategory(soup)
        postToFB(category, title, body)
    else:
        print("checked {}, not found".format(webid))
        time.sleep(10)
