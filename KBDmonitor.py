import winsound
import random
# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

while True:
    # set the url as VentureBeat,
    url = "https://kbdfans.com/products/kbd67v2"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    # parse the downloaded homepage and grab all text, then,
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text.lower(), "lxml")
    temp = soup.findAll(text=lambda text: text and "sold out" in text)
    if len(temp) != 7:
        for i in range(10000000):
            winsound.PlaySound("check-website-now1571517818 (online-audio-converter.com).wav", winsound.SND_FILENAME)
            i+=1
    else:
        print("retry")
        i = random.randrange(240,360)
        time.sleep(i)
