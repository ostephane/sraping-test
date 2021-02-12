import requests
from bs4 import BeautifulSoup
url = 'https://books.toscrape.com/'
response = requests.get(url)
if response.ok:
    s=BeautifulSoup(response.text)
    print(s)
    title=s.find('title')
    print(title.txt)
