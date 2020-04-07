import requests
from bs4 import BeautifulSoup

URL = 'https://www.predictit.org/api/marketdata/markets/4292/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='4292')


print(page.text)

