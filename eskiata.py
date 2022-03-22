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

site = 'https://www.haremaltin.com/altin-fiyatlari'

wd = webdriver.Chrome('chromedriver', options=options)

wd.get(site)

time.sleep(5) 

html = wd.page_source

df = pd.read_html(html)

eski_ata= df[1][2][15]
eski_ata = int((float(eski_ata))*1000)
toplampara = int(input('Elimizdeki para: '))

adet = int((toplampara / eski_ata))
kalan = toplampara - (eski_ata * adet)

print(f"Eski ata lira fiyatı {eski_ata} TL. Elimizdeki para ile {adet} adet ata lira alabiliriz ve geriye {kalan} lira para kalır.")