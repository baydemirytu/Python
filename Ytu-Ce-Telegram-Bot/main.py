import time
import requests
import telegram
from bs4 import BeautifulSoup

def main():
    bot = telegram.Bot("YOUR TELEGRAM BOT API KEY")
    html_file = requests.get('https://ytuce.maliayas.com/').text
    soup = BeautifulSoup(html_file, 'lxml')
    ilk_baslik = soup.find('div', class_='text_title').text

    while 1:
        html_file = requests.get('https://ytuce.maliayas.com/').text
        soup = BeautifulSoup(html_file, 'lxml')
        baslik = soup.find('div', class_='text_title').text

        if ilk_baslik != baslik:
            gonderi = soup.find('div', class_='text_title').a
            text = str(gonderi)
            index = text.rfind("href=")
            index_son = text.rfind("target")
            link = text[index + 6:index_son - 2]

            bot.send_message(CHANNEL CODE, link)
            bot.send_message(CHANNEL CODE, "Diğer duyurular için -> https://ytuce.maliayas.com/")
            ilk_baslik = baslik
        time.sleep(3*60)

main()
