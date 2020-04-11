import requests
import re
from urllib2 import urlopen
from bs4 import BeautifulSoup


url = 'https://www.predictit.org/api/marketdata/markets/4292'
soup = BeautifulSoup(urlopen(url).read() , 'html5lib')

results = soup(text = re.compile('bestBuyYesCost'))
# results[0].split('" ')
newr = results[0].split()
itr = 0
print newr[51]
newr[51] = newr[51][:-1]
#This is the byYesCost
print newr[51]

print newr[53]
newr[53] = newr[53][:-1]
#This is the buyNoCost
print newr[53]