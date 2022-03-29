import requests
from bs4 import BeautifulSoup

# response = requests.get("https://stopklatka.pl/?s=czterej+pancerni")
#
# soup = BeautifulSoup(response.text, "html.parser")
# # print(soup)
# print(soup.find_all(name="span", calss_="date film"))
# dni_emisji = [dzien.getText() for dzien in soup.find_all(name="span", class_="date film", limit=5)]
# print(dni_emisji)
# data = soup.select("span")
# print(data)
# reworked = data.find_all(class_="emisjaDzien")

response2 = requests.get("https://www.telemagazyn.pl/serial/czterej-pancerni-i-pies-553609/")

soup2 = BeautifulSoup(response2.text, "html.parser")

dni_emisji2 = [dzien.getText() for dzien in soup2.find_all(name="span", class_="emisjaDzien", limit=5)]
# print(dni_emisji2)

kanal_emisji = [kanal.getText().strip() for kanal in soup2.find_all( name=['div','p',"a"],class_=['emisjaSzczegoly'] , limit=5)]
# print(kanal_emisji)
message='Najbliższe odcinki 4 pancernych i psa to :\n'
temp=[]
for emisja in kanal_emisji:
    temp = emisja.split('\n')
    # temp.split('''\n''')
    # temp.remove('')
    # temp.remove('')
    # print(temp)
    message+= f'Dzień emisji {temp[0]}\n' \
              f'Godzina emisji {temp[1]}\n' \
              f'Odcinek {temp[2]}\n' \
              f'Kanał {temp[5]} \n'
# print(temp)
print(message)