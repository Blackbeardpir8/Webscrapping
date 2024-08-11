import requests
from bs4 import BeautifulSoup


def scrap_imdb_news():
    url = "https://www.imdb.com/news/movie/"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',

    }
    
    response = requests.get(url,headers=headers)
    print(response.text)

scrap_imdb_news()

