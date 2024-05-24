import requests
from bs4 import BeautifulSoup

url = 'https://food-fantasy.fandom.com/wiki/Recipes'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
for row in soup.find_all('tr'):
    data = row.find_all('td')
    if len(data) == 5:
        item = data[0].text.strip()
        desc = data[1].text.strip()
        desc2 = data[2].text.strip()
        desc3 = data[3].text.strip()
        if desc2 != '':
            print(f'|{item} | {desc}, {desc2}')
        elif desc3 != '':
            print(f'|{item} | {desc}, {desc2}, {desc3}')
        else:
            print(f'|{item} | {desc}')

