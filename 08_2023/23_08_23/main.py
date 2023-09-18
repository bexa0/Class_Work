# from bs4 import BeautifulSoup
import requests
# import pandas as pd
# import openpyexcel
#
# url = 'https://www.google.com/?hl=RU'
#
# page_main = requests.get(url)
# soup = BeautifulSoup(page_main.text, features='html.parser')
#
# catalog = soup.find('div', {'id': 'SIvCob'}).text
# print(catalog)

# df = pd.DataFrame(catalog)
# df.to_excel('team1.xlsx')



# link = catalog.find('a')['href']
# page_catalog = requests.get('https://www.parsemachine.com' + link)
# soup = BeautifulSoup(page_catalog.text, features='html.parser')
#
# count = soup.find_all('div', {'class': 'card product-cart'})
# for x in count:
#     print(x.find('img')['alt'])
#     print(x.find('img')['src'])
#     print(x.find('a')['href'])
#     print()




from selenium import webdriver
import time
import os


browser = webdriver.Chrome()
browser.get('http://www.google.com')
time.sleep(2)
os.system('team1.xlsx')
