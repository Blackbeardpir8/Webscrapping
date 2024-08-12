import requests
from bs4 import BeautifulSoup

def scrap_imdb_news():
    url = "https://www.imdb.com/news/movie/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    news_items = soup.find_all('div', class_='ipc-list-card--border-line')

    for item in news_items:
        
        title_element = item.find('a', class_="ipc-link ipc-link--base sc-bec740f7-3 gBbzGe")
        title = title_element.text.strip() if title_element else "No Title"
        
       
        description_element = item.find('div', class_="ipc-html-content-inner-div")
        description = description_element.text.strip() if description_element else "No Description"
        
       
        image_element = item.find('img', class_="ipc-image")
        image = image_element['src'] if image_element else "No Image"
        
        
        external_link = title_element['href'] if title_element else "No Link"

        articles.append({
            'title': title,
            'description': description,
            'image': image,
            'external_link': external_link,
        })

    # Print the first article to verify
    print(articles[0])

scrap_imdb_news()
