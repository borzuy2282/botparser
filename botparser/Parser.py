import requests
from bs4 import BeautifulSoup as b

URL = 'https://petition.president.gov.ua/?status=active&sort=votes&order=desc'
def parseTitle(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    petitions = soup.find_all('a', class_='pet_link')
    return [c.text for c in petitions]
def parseUrl(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    petitions = soup.find_all('a', class_='pet_link')
    return [c.get('href') for c in petitions]
# print(*parseTitle(URL), sep='\n')
# print(*parseUrl(URL), sep='\n')