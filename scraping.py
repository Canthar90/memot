import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json


class Scrapping():
    def __init__(self):
        pass


    def pancernioki(self):
        """Simple scrapping for my father in law"""
        pancerniaki_response = requests.get("https://www.telemagazyn.pl/serial/czterej-pancerni-i-pies-553609/")

        pancerniaki_soup = BeautifulSoup(pancerniaki_response.text, "html.parser")


        emisja_info = [kanal.getText().strip() for kanal in pancerniaki_soup.find_all( name=['div','p',"a"],class_=['emisjaSzczegoly'] , limit=5)]
        message = 'Najbliższe odcinki 4 pancernych i psa to :\n'
        temp = []
        for emisja in emisja_info:
            temp = emisja.split('\n')

            message += f'Dzień emisji {temp[0]}\n' \
                       f'Godzina emisji {temp[1]}\n' \
                       f'Odcinek {temp[2]}\n' \
                       f'Kanał {temp[5]} \n\n'
        # print(temp)
        return message


class Allegro_scrapping():
    """Scraping allegro with sellenium"""
    def __init__(self):
        try:
            with open("planned.json") as file:
                self.planned = json.load(file)
        except:
            self.planned = {}


    def search(self, search_word, search_number=1, by_pricve=False):
        '''this function will search the search_word and retutrn message containing selected search_number of
            search reasults '''

        chrome_driver = "./chromedriver/chromedriver.exe"
        s = Service(chrome_driver)
        options = ChromeOptions()
        driver = webdriver.Chrome(service=s, options=options)
        action = ActionChains(driver=driver)
        time.sleep(1)

        driver.get("https://allegro.pl")

        time.sleep(1)
        action.key_down(Keys.ENTER)
        action.key_up(Keys.ENTER)
        action.perform()

        time.sleep(1)
        search_pole = driver.find_element(
            By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div/div/div[3]/header/div/div/div/div/form/input")

        # /html/body/div[3]/div[3]/div/div/div/div/div/div[3]/header/div/div/div/div/form/input
        action.click(on_element=search_pole)
        action.send_keys(search_word)
        action.key_down(Keys.ENTER)
        action.key_up(Keys.ENTER)
        action.perform()

        if by_pricve == 'True':
            time.sleep(1)
            sorting_selector = driver.find_element(
                By.XPATH,
                """/html/body/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div[3]/div[3]/div/div/div/select""")

            action.click(on_element=sorting_selector)
            action.key_down(Keys.ARROW_DOWN)
            action.key_up(Keys.ARROW_DOWN)
            action.key_down(Keys.ENTER)
            action.key_up(Keys.ENTER)
            action.perform()

        time.sleep(2)

        main_titles = driver.find_elements(
            By.CSS_SELECTOR,
            """div div div div div div div div div div div div div div div section article div div div h2 a"""
        )

        main_prices = driver.find_elements(
            By.CSS_SELECTOR,
            """div div div div div div div div div div div div div div div section article div div div div div span._1svub._lf05o"""
        )


        if len(main_titles) == 0:
            return 'Sory nie mogę znaleźć wyników dla tego zapytania'
        else:
            message = ''
            count = 0
            for title in main_titles:
                message += f"""Tytuł to: {main_titles[count].text}\nCena to {main_prices[count].text}\n"""
                message += f"""link: {main_titles[count].get_attribute('href')} \n"""
                count += 1
                if count == int(search_number):
                    driver.quit()
                    return message

            message += "Nie było wystarczająco dużo wyników wyszukiwania"
            driver.quit()
            return message

    def single_search(self, fraze):
        """Define how to act depending on passed input"""
        if len(fraze) == 1:
            message = self.search(search_word=fraze[0])
            return message
        elif len(fraze) == 2:
            message = self.search(search_word=fraze[0], search_number=fraze[1])
            return message
        elif len(fraze) == 3:
            message = self.search(search_word=fraze[0], search_number=fraze[1], by_pricve=fraze[2])
            return message

