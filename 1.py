import requests
from bs4 import BeautifulSoup
r=
requests.get('https://humanities.jejunu.ac.kr/humanities/community/notice.htm?page=1')
print(r.text)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)