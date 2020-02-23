# Import Libriries
import requests
from bs4 import BeautifulSoup

# Take the page where you want to work and make soup object from page
page = requests.get('https://www.iee.ihu.gr/udg_courses')
soup = BeautifulSoup(page.content, 'html.parser')

# Lists to store the scraped data in
courses = []

# Extract data
# Take 7th table(table[6] because start from zero) for 7th semester.
table_7 = soup.findAll('table')[6]
# Take all tr from table_7
for tr in table_7.findAll('tr'):
    # Take all td with attribute "title" because there are some without title(They don't need)
    for td in tr.findAll('td', {"title" : True}):
        # Add course from td in courses list
        courses.append(td['title'])
        # Write to file
        with open("log.txt", 'a', encoding='utf8') as f:
            f.write(courses[-1]+"\n")