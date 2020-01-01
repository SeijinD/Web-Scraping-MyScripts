import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://meteo.gr/lab/book/index.cfm?city_id=1')
soup = BeautifulSoup(page.content, 'html.parser')

# Lists to store the scraped data in
days = []
temperatures = []
# Extract data from individual dayblock
for block in soup.find_all(class_ = 'dayblock'):
    day = block.find(class_ = 'subheader_calendar')
    # Data Number and Month Name
    dom = block.find(class_ = 'datenumber_calendar').get_text()
    month = block.find(class_ = 'month_calendar').get_text()
    daystr = f"{dom} {month}"
    days.append(daystr)
    # Low and High Temperature
    hightemp = block.find(class_ = 'hightemp').get_text()
    lowtemp = block.find(class_ = 'lowtemp').get_text()
    tempstr = f"{lowtemp} {hightemp}"
    temperatures.append(tempstr)

# Print in Table with Pandas
weather_table = pd.DataFrame({
    'Days' : days,
    'Temperatures' : temperatures
})

# Extract to the csv file
weather_table.to_csv('week_weather.csv')