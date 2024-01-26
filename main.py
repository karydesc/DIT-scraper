import time

import requests
from bs4 import BeautifulSoup

def formURL(num):
    return "https://www.dit.uoi.gr/news.php?sa=view_new&id=" + str(num)


def getBody(obj):
    return obj.find("div", class_="chris").getText()

def getTitle(obj):
    temp =  obj.find("h1", class_="title")
    return temp.getText()

def getSubtitle(obj):
    temp = obj.find("h2", class_="subtitle")
    return temp.getText()

def getCategory(obj):
    category_element = obj.find('b', string='Κατηγορία:')
    temp = category_element.find_next_sibling(string=True).strip()
    return temp

def postToFB(imgcat,title_,body_):
    match imgcat:
        case "Διάλεξη":
    post_url = 'https://graph.facebook.com/{}/photos'.format(page_id)
    file = {"source" : open(image_path, 'rb')}
    payload = {
        "access_token": access_token,
        "message": title_ + "\n\n\n\n\n\n\n" + body_,


    }
    r = requests.post(post_url, data=payload,files=file)
    print(r.text)

photo_grammateia = "122115918656171640"
access_token = "EAAM0b8NuPY0BOzszfKgrQUZBDc1gYyAZCBu70ryzIpbSQ2C45rJ3omsRGaOtEZCfVlJYsfgE3bNZAV8IQlyhSXXkBkfXAO5ahLqayOy9EU7xZChTsjwT3eyZA9BIZA1UZAZBiykMMQvBCXxkFwJPK1TRO9M7Mw9ACVs4jL3sODk9oX4wZBDmVKX6APmxmMdXoVQccZD"
page_id = "209342058929085"
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
    URL = formURL(webid)
    if not check404(URL):
        print("found at "+str(webid))
        webid += 1
        writeNewID(webid) #write to file the incremented id for which the loop will continue searching
        page = requests.get(URL) #
        soup = BeautifulSoup(page.content, "html.parser")

        body = getBody(soup)
        title = getTitle(soup)
        #subtitle = getSubtitle(soup)
        category = getCategory(soup)

        postToFB(0, title, body)
    else:
        print("checked {}, not found".format(webid))
        time.sleep(10)





