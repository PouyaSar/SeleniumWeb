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

def read_card_list(filename):
    card_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(' ', 1)
            if len(parts) == 2:
                card_list.append(parts[1])
    return card_list

def main():
    card_list = read_card_list('card_list.txt')
    total = 0
    priced_cards = []
    driver = webdriver.Chrome()
    for cards in card_list:
        card_fixed = cards.replace(" ", "+")
        cardurl = "https://www.tcgplayer.com/search/magic/product?productLineName=magic&q="+card_fixed+"&view=grid&RarityName=Rare|Mythic|Uncommon|Common|Promo|Land"
        driver.get(cardurl)
        currentmoney = 50
        try:
            listings = WebDriverWait(driver, 500).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-card__content'))
        )
            for listing in listings:
                if bool(listing.find_elements(By.CLASS_NAME, 'inventory__price-with-shipping')):
                    name = WebDriverWait(listing, 500).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'product-card__title'))
                    ).text
                    price = WebDriverWait(listing, 500).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'inventory__price-with-shipping'))
                    ).text
                    if (cards in name):
                        money = price
                        money_cleaned = money.replace("$", "")
                        money_cleaned = money_cleaned.replace(",", "")
                        money_float = float(money_cleaned)
                        if (currentmoney > money_float):
                            currentmoney = money_float
                else:
                    continue
            total = total + currentmoney
            priced_cards.append((cards, currentmoney))
        finally:
            pass

    priced_cards = sorted(priced_cards, key=lambda item: item[1], reverse=True)
    with open("Priced.txt", 'w', encoding='utf-8') as file:
        for cards, price in priced_cards:
            file.write(cards + ": " + str(price) + "\n")
        file.write("Total: " + str(total) + "\n")

'''
try:
    listings = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-card__content'))
)
    for listing in listings:
        name = listing.find_element(By.CLASS_NAME, 'product-card__title truncate').text
        price = listing.find_element(By.CLASS_NAME, 'inventory__price-with-shipping').text
        if (cards in name):
            money = price
            money_cleaned = money.replace("$", "")
            money_float = float(money_cleaned)
            if (currentmoney > money_float):
                currentmoney = money_float
        total = total + currentmoney
        with open("Priced.txt", 'a') as file:
            file.write(cards+": "+str(currentmoney)+"\n")
    with open("Priced.txt", 'a') as file:
            file.write("Total: "+str(total)+"\n")
finally:
    pass
'''

#print(currentmoney)
#write_csv(data)
main()

time.sleep(2)

'''
old:  
def main():
    total = 0
    for cards in card_list:
        card_fixed = cards.replace(" ", "+")
        cardurl = "https://www.tcgplayer.com/search/magic/product?productLineName=magic&q="+card_fixed+"&view=grid"
        driver = webdriver.Chrome()
        driver.get(cardurl)
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
        total = total + currentmoney
        with open("Priced.txt", 'a') as file:
            file.write(cards+": "+str(currentmoney)+"\n")
    with open("Priced.txt", 'a') as file:
            file.write("Total: "+str(total)+"\n")
'''