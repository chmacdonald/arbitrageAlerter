import requests
import re
from urllib2 import urlopen
from bs4 import BeautifulSoup


url = 'https://webcache.googleusercontent.com/search?q=cache:YOtEggQzgjAJ:https://www.bovada.lv/sports/politics/us-politics+&cd=2&hl=en&ct=clnk&gl=us'
soup = BeautifulSoup(urlopen(url).read() , 'html5lib')

print soup

# results = soup(text = re.compile('bestBuyYesCost'))
# # results[0].split('" ')
# newr = results[0].split()
# itr = 0
# print newr[51]
# newr[51] = newr[51][:-1]
# #This is the byYesCost
# print newr[51]

# print newr[53]
# newr[53] = newr[53][:-1]
# #This is the buyNoCost
# print newr[53]