import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

card_list = [
"Abuelo, Ancestral Echo",
    "Academy Manufactor",
    "Against All Odds",
    "Arcane Denial",
    "Arcane Sanctum",
    "Arcane Signet",
    "Austere Command",
    "Azorius Signet",
    "Baleful Strix",
    "Bojuka Bog",
    "Caves of Koilos",
    "Choked Estuary",
    "Cleansing Nova",
    "Cloudshift",
    "Command Tower",
    "Counterspell",
    "Cranial Plating",
    "Curtains' Call",
    "Cyberdrive Awakener",
    "Dark Ritual",
    "Darksteel Mutation",
    "Darkwater Catacombs",
    "Dawnbringer Cleric",
    "Deadeye Navigator",
    "Dimir Signet",
    "Dovin's Veto",
    "Dusk Legion Zealot",
    "Eerie Interlude",
    "Ephemerate",
    "Essence Flux",
    "Fellwar Stone",
    "Flicker of Fate",
    "Generous Gift",
    "Ghostly Flicker",
    "Glacial Floodplain",
    "Goldmire Bridge",
    "Grasp of Fate",
    "Ice Tunnel",
    "Illusion of Choice",
    "Imprisoned in the Moon",
    "Inspiring Statuary",
    "Island",
    "Kappa Cannoneer",
    "Lae'zel's Acrobatics",
    "Lobelia Sackville-Baggins",
    "Lobelia, Defender of Bag End",
    "Lotho, Corrupt Shirriff",
    "Marionette Master",
    "Massacre Wurm",
    "Memory Lapse",
    "Mirkwood Bats",
    "Mistmeadow Witch",
    "Mistvault Bridge",
    "Momentary Blink",
    "Mystic Remora",
    "Obscura Storefront",
    "Orzhov Signet",
    "Panharmonicon",
    "Path to Exile",
    "Plains",
    "Port Town",
    "Razortide Bridge",
    "Rise and Shine",
    "Shineshadow Snarl",
    "Slip On the Ring",
    "Snowfield Sinkhole",
    "Sol Ring",
    "Soulherder",
    "Sun Titan",
    "Supreme Verdict",
    "Swamp",
    "Swords to Plowshares",
    "Talisman of Dominance",
    "Talisman of Hierarchy",
    "Talisman of Progress",
    "Teleportation Circle",
    "Time Sieve",
    "Touch the Spirit Realm",
    "Turn to Mist",
    "Twining Twins",
    "Void Rend",
    "Wash Away",
    "Whirlwind Denial",
    "Tivit, Seller of Secrets"
]

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
""""
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
"""
    
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


#print(currentmoney)
#write_csv(data)
main()

time.sleep(2)
