import requests
from bs4 import BeautifulSoup
from scrapping.models import News
import uuid
import os
import requests


def download_image(image_url,save_directory, image_name):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    image_path = os.path.join(save_directory,image_name)
    response = requests.get(image_url,stream = True)
    if response.status_code == 200:
        with open(image_name,'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    
    return image_url


def scrap_imdb_news():
    url = "https://www.imdb.com/news/movie/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = soup.find_all('div', class_='ipc-list-card--border-line')

    for item in news_items:
        
        title_element = item.find('a', class_="ipc-link ipc-link--base sc-bec740f7-3 gBbzGe")
        title = title_element.text.strip() if title_element else "No Title"
        
       
        description_element = item.find('div', class_="ipc-html-content-inner-div")
        description = description_element.text.strip() if description_element else "No Description"
        
       
        image_element = item.find('img', class_="ipc-image")
        image = image_element['src'] if image_element else "No Image"

        image_path = None
        if image:
            image_name = f"image_{uuid.uuid4()}.jpg"
            image_path = download_image(image,'downloads',image_name)

        
        external_link = title_element['href'] if title_element else "No Link"

        news = {
            'title': title,
            'description': description,
            'image': image,
            'external_link': external_link,
        }

        News.objects.create(**news)


