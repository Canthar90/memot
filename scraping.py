from lib2to3.pgen2 import driver
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time


class Scrapping():

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
        return message


class Allegro_scrapping():
    """Scraping allegro with sellenium"""
    def __init__(self):
        try:
            with open("planned.json") as file:
                self.planned = json.load(file)
        except:
            self.planned = {}


    def search(self, search_word: str, search_number: int=1, by_pricve: bool=False) -> str:
        '''this function will search the search_word and retutrn message containing selected search_number of
            search reasults '''

        if type(search_word) != str:
            raise ValueError("Invalid data type in search_word expected str")
        elif type(search_number) != int:
            raise ValueError("Invalid data type in search_number expected int")
        elif type(by_pricve) != bool:
            raise ValueError("Invalid data type in by_price expected bool")
        else:
            
            chrome_driver = "./chromedriver/chromedriver.exe"
            s = Service(chrome_driver)
            options = ChromeOptions()
            driver = webdriver.Chrome(service=s, options=options)
            action = ActionChains(driver=driver)
            wait = WebDriverWait(driver, 10)
            

            driver.get("https://allegro.pl")

            cookies_agreement = wait.until(EC.element_to_be_clickable((By.XPATH,
            """//*[@id="opbox-gdpr-consents-modal"]/div/div[2]/div/div[2]/button[1]""")))
            
            action.click(on_element=cookies_agreement)
            action.perform()
            
            
            
            search_pole = wait.until(EC.visibility_of_element_located((
                By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div/div[3]/header/div/div/div/div/form/input"
            )))

            

            action.click(on_element=search_pole)
            action.send_keys(search_word)
            action.key_down(Keys.ENTER)
            action.key_up(Keys.ENTER)
            action.perform()

            if by_pricve:
                
                sorting_selector = wait.until(EC.visibility_of_element_located((
                    By.XPATH,
                    """//*[@id="allegro.listing.sort"]""")))
                
                action.click(on_element=sorting_selector)
                action.key_down(Keys.ARROW_DOWN)
                action.key_up(Keys.ARROW_DOWN)
                action.key_down(Keys.ENTER)
                action.key_up(Keys.ENTER)
                action.perform()
                time.sleep(2)
                
                
                

            try:
                invalid = driver.find_element(By.XPATH,
                    """/html/body/div[2]/div[4]/div/div/div/div/div/div[2]/section/h1""")
                
                return 'Sory nie mogę znaleźć wyników dla tego zapytania'
                
            except:

                wait.until(EC.visibility_of_element_located((By.XPATH,
                    """//*[@id="search-results"]/div[6]/div/div/div[1]/div/div/section/article/div/div/div[2]/div[1]/h2/a""")))

                main_titles = driver.find_elements(
                    By.XPATH,
                    """//*[@id="search-results"]/div[6]/div/div/div[1]/div/div/section/article/div/div/div[2]/div[1]/h2/a""")
                

                main_prices = driver.find_elements(
                    By.XPATH, 
                    """//*[@id="search-results"]/div[6]/div/div/div[1]/div/div/section/article/div/div/div[2]/div[2]/div/div/span""")
                
                

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
                
                

class XcomScraping:
    """Simple scraping on demand from xcom webside """

    
    def search(self, question: str, number: int = 1, flag: bool = False) -> None:
        """Search for reasults on xcom depending on the inputs flag is sorting 
        from the cheapest reasult"""
        self.check_for_errors(question=question, number=number, flag=flag)
    
    
    def check_for_errors(self, question: str, number: int, flag: bool) -> None:
        """Checks data formats of inputs from outside"""
        if type(question) != str:
            raise ValueError("Bad value type expected str for question")
        elif type(number) != int:
            raise ValueError("Bad value type expected int for number")
        elif type(flag) != bool:
            raise ValueError("Bad value type expected bool for flag")
        else:
            self.checking(question=question, number=number, flag=flag)
            
            
    def checking(self, question: str, number: int, flag: bool):
        """Makest the scrapping work"""
        
        chrome_driver = "./chromedriver/chromedriver.exe"
        s = Service(chrome_driver)
        options = ChromeOptions()
        driver = webdriver.Chrome(service=s, options=options)
        action = ActionChains(driver=driver)
        wait = WebDriverWait(driver, 10)
        
        driver.get("https://www.x-kom.pl/")
        click = wait.until(EC.element_to_be_clickable ((By.XPATH, "/html/body/div[2]/div[10]/div/div/div/div[1]/div/div/h3")))

        action.click(on_element = click)
        action.key_down(Keys.TAB)
        action.key_up(Keys.TAB)
        action.key_down(Keys.TAB)
        action.key_up(Keys.TAB)
        action.key_down(Keys.TAB)
        action.key_up(Keys.TAB)
        action.key_down(Keys.ENTER)
        action.key_up(Keys.ENTER)
        action.perform()
        time.sleep(10)



xsearch = XcomScraping()
xsearch.search("rtx 3070")
