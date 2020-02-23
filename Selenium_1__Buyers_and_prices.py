from selenium import webdriver
import csv

MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3

with open('result.csv', 'w', encoding='utf8') as f:
    f.write("Buyers, Price \n")

# Set driver with Firefox webdriver
driver = webdriver.Firefox(executable_path="C:\\Python\\Tools\\geckodriver.exe")

# Make loop for run all pages
for i in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" +str(i)
    url = "https://econpy.pythonanywhere.com/ex/" + page_num + ".html"
    driver.get(url)

    # Get buyers and prices by xpath
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

    # Write all buyers+prices in result.csv
    with open('result.csv', 'a', encoding='utf8') as f:
        f.write("Page" + str(i) + "\n")
        for j in range(len(buyers)):
            f.write(str(j) + ") " + buyers[j].text + " : " + prices[j].text + "\n")
        
# Close driver
driver.close()