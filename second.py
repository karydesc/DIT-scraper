import requests

def upload_image(access_token, page_id, image_path):
    # Upload the image
    upload_url = f"https://graph.facebook.com/{page_id}/photos"
    files = {'source': open(image_path, 'rb')}
    params = {'access_token': access_token}
    response = requests.post(upload_url, files=files, params=params)
    data = response.json()

    # Get the image ID from the response
    if 'id' in data:
        image_id = data['id']
        print("Image uploaded successfully! Image ID:", image_id)
        return image_id
    else:
        print("Failed to upload image. Response:", data)
        return None

if __name__ == "__main__":
    # Your Facebook access token and page ID
    access_token = "EAAM0b8NuPY0BOzszfKgrQUZBDc1gYyAZCBu70ryzIpbSQ2C45rJ3omsRGaOtEZCfVlJYsfgE3bNZAV8IQlyhSXXkBkfXAO5ahLqayOy9EU7xZChTsjwT3eyZA9BIZA1UZAZBiykMMQvBCXxkFwJPK1TRO9M7Mw9ACVs4jL3sODk9oX4wZBDmVKX6APmxmMdXoVQccZD"
    page_id = "209342058929085"

    # Path to the local image file
    image_path = "/Users/chris/Documents/repos/DIT-scraper/artworks-zyYqA8D0BdfuyH28-WeeHrw-t500x500.jpg"

    upload_image(access_token, page_id, image_path)
