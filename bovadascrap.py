import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'

}
with requests.Session() as s:
    url = "https://www.bovada.lv/sports/politics"
    r = s.get(url, headers = headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup)