import time

import requests
from bs4 import BeautifulSoup



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


        post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)
        payload = {
            "access_token": access_token,
            "message": title.getText() + "\n" +body.getText(),
            "source" : "https://i1.sndcdn.com/artworks-zyYqA8D0BdfuyH28-WeeHrw-t500x500.jpg"
        }
        r = requests.post(post_url, data=payload)
        print(r.text)
        continue

    print("not found")
    time.sleep(5)





