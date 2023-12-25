import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def page(card):
    card_fixed = card.replace(" ", "+")
    cardurl = "https://www.tcgplayer.com/search/magic/product?productLineName=magic&q="+card_fixed+"&view=grid"
    driver = webdriver.Chrome()
    driver.get(cardurl)

'''def write_csv(data):
   with open('selenium_ex.csv', 'a') as f:
       writer = csv.writer(f)
       writer.writerow((data['money']))
'''

site = "https://www.tcgplayer.com/search/magic/product?productLineName=magic&q=tyrranax+rex&view=grid"
driver = webdriver.Chrome()
driver.get(site)
try:
    elements = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory__price-with-shipping'))
    )
finally:
    pass
currentmoney = 50.0
for element in elements:
    money = element.text
    money_cleaned = money.replace("$", "")
    money_float = float(money_cleaned)
    if (currentmoney > money_float):
        currentmoney = money_float
    

print(currentmoney)
#write_csv(data)

time.sleep(10)
