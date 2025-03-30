import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

card_list = [
    "Rimewood Falls",
    "Access Tunnel",
    "Acidic Slime",
    "Adaptive Automaton",
    "Arcane Signet",
    "Archpriest of Shadows",
    "Beast Whisperer",
    "Beast Within",
    "Bident of Thassa",
    "Binding the Old Gods",
    "Biogenic Ooze",
    "Biowaste Blob",
    "Bloodline Pretender",
    "Champion of Lambholt",
    "Coastal Piracy",
    "Command Tower",
    "Consuming Blob",
    "Convert to Slime",
    "Crippling Fear",
    "Cultivate",
    "Deathsprout",
    "End-Raze Forerunners",
    "Enduring Curiosity",
    "Eternal Witness",
    "Exotic Orchard",
    "Experiment Kraj",
    "Experiment One",
    "Garruk's Uprising",
    "Gelatinous Cube",
    "Gelatinous Genesis",
    "Golgari Charm",
    "Green Slime",
    "Harrow",
    "Haunted Mire",
    "Herald's Horn",
    "Icon of Ancestry",
    "Infernal Grasp",
    "Invasion of Zendikar",
    "Kodama's Reach",
    "Manaplasm",
    "Mwonvuli Acid-Moss",
    "Nature's Lore",
    "Necrotic Ooze",
    "Ochre Jelly",
    "Ohran Frostfang",
    "One with Nature",
    "Opulent Palace",
    "Oran-Rief, the Vastwood",
    "Path of Ancestry",
    "Prime Speaker Vannifar",
    "Rampant Growth",
    "Ravenous Slime",
    "Realmwalker",
    "Reconnaissance Mission",
    "Return of the Wildspeaker",
    "Rogue's Passage",
    "Scavenging Ooze",
    "Shamanic Revelation",
    "Skyshroud Claim",
    "Sludge Monster",
    "Sol Ring",
    "Strixhaven Stadium",
    "Sunken Hollow",
    "Tangled Islet",
    "Temperamental Oozewagg",
    "Temple of Deceit",
    "Temple of Malady",
    "Temple of Mystery",
    "The Key to the Vault",
    "The Mimeoplasm",
    "Timeless Witness",
    "Uchuulon",
    "Ulvenwald Oddity",
    "Umori, the Collector",
    "Vanquisher's Banner",
    "Voidslime",
    "Woodland Chasm",
    "Yavimaya Coast",
]

def page(card):
    card_fixed = card.replace(" ", "+")
    cardurl = "https://www.tcgplayer.com/search/magic/product?productLineName=magic&q="+card_fixed+"&view=grid"
    driver = webdriver.Chrome()
    driver.get(cardurl)

def main():
    total = 0
    for cards in card_list:
        card_fixed = cards.replace(" ", "+")
        cardurl = "https://www.tcgplayer.com/search/magic/product?productLineName=magic&q="+card_fixed+"&view=grid&RarityName=Rare|Mythic|Uncommon|Common|Promo|Land"
        driver = webdriver.Chrome()
        driver.get(cardurl)
        currentmoney = 50
        try:
            listings = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-card__content'))
        )
            for listing in listings:
                if bool(listing.find_elements(By.CLASS_NAME, 'inventory__price-with-shipping')):
                    name = WebDriverWait(listing, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'product-card__title'))
                    ).text
                    price = WebDriverWait(listing, 20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'inventory__price-with-shipping'))
                    ).text
                    if (cards in name):
                        money = price
                        money_cleaned = money.replace("$", "")
                        money_float = float(money_cleaned)
                        if (currentmoney > money_float):
                            currentmoney = money_float
                else:
                    continue
            total = total + currentmoney
            with open("Priced.txt", 'a') as file:
                file.write(cards+": "+str(currentmoney)+"\n")
        finally:
            pass
    with open("Priced.txt", 'a') as file:
        file.write("Total: "+str(total)+"\n")

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