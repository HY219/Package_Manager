import requests
from bs4 import BeautifulSoup
r = requests.get('file:///C:/Users/jhy_0/2021-1/Package_Manager/2.html')
print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.p)