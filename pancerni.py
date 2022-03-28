import requests
from bs4 import BeautifulSoup

response = requests.get("https://stopklatka.pl/?s=czterej+pancerni")

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
print(soup.find_all(name="span", calss_="date film"))
dni_emisji = [dzien.getText() for dzien in soup.find_all(name="span", class_="date film")]
print(dni_emisji)
# data = soup.select("span")
# print(data)
# reworked = data.find_all(class_="emisjaDzien")

response2 = requests.get("https://www.telemagazyn.pl/serial/czterej-pancerni-i-pies-553609/")

soup2 = BeautifulSoup(response2.text, "html.parser")

dni_emisji2 = [dzien.getText() for dzien in soup2.find_all(name="span", class_="emisjaDzien")]
print(dni_emisji2)