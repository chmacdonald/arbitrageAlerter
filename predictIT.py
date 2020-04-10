# import requests
# import csv
# import xml.etree.ElementTree as ET
# from bs4 import BeautifulSoup
# URL = 'https://www.predictit.org/api/marketdata/markets/4292/'
# xml = requests.get(URL)
# page = ET.parse(xml)
# # soup = BeautifulSoup(page.content, 'XML.parser')
# # results = soup.find(id='4292')
# print(page.text)
import urllib2
import xmltodict
file = urllib2.urlopen('https://www.predictit.org/api/marketdata/markets/4292/')
data = file.read()
file.close()

data = xmltodict.parse(data)
print(render_to_response('my_template.html', {'data': data}))