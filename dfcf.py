import numpy as np
import requests
from bs4 import BeautifulSoup

url = 'http://quote.eastmoney.com/center/'
resource = requests.get(url)
soup = BeautifulSoup(resource.text, 'lxml')

print(soup)