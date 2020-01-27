import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
links = []

page = requests.get('https://cerebrux.net/page/1')

html_soup = BeautifulSoup(page.content, 'html.parser')

article = html_soup.find_all('article')

for block in article:
    title = block.find(class_ = 'entry-title').get_text()
    titles.append(title)
    for a in  block.find(class_ = 'entry-title'):
        link = a['href']
        links.append(link)

cerebrux_articles = pd.DataFrame({'Title': titles, 'Link' : links})
cerebrux_articles

cerebrux_articles.to_csv('cerebrux_articles.csv')