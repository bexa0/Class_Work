from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import requests
#
# url = 'https://www.google.com/search?q'
# a = requests.get(url)
driver = webdriver.Chrome()
driver.get('https://www.gismeteo.ru/weather-tashkent-5331/month/')
time.sleep(5)
w = driver.find_element(By.CLASS_NAME, 'maxt')
print(w.text)
time.sleep(1)

driver.close()
driver.quit()