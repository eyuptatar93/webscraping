from selenium import webdriver
import pandas as pd
import time

# pip install selenium
# apt-get update # to update ubuntu to correctly run apt install
# apt install chromium-chromedriver
# cp /usr/lib/chromium-browser/chromedriver /usr/bin

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

website = 'https://www.haremaltin.com/altin-fiyatlari'

wd = webdriver.Chrome('chromedriver', options=options)

wd.get(website)

time.sleep(5) 

html = wd.page_source

df = pd.read_html(html)

eski_ata = df[1][2][15]
eski_ata = int((float(eski_ata))*1000) # converts the str into float and then the float value into int
cash = int(input('The money we have: '))

piece = int((cash / eski_ata))
rest = cash - (eski_ata * piece)

print(f"It costs {eski_ata} TL. We can buy {piece} 'Ata Lira' gold and {rest} lira left.")
