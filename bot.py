import os
import random

import time

from datetime import datetime

import discord
import json
from scraping import Scrapping, Allegro_scrapping
import asyncio
from datson import Garbagson
from apis import Weather_forecasting
import gc


with open("starting.json") as start:
    starting = json.load(start)

# TOKEN = 'token'
TOKEN = starting['token']

client = discord.Client()

scrap = Scrapping()

weather = Weather_forecasting()

@client.event  # oto element logujacy
async def on_ready():
    print('We are login as {0.user}'.format(client))






jarkendar = client.get_channel(starting['jarkendar'])
samo_jedzonko = client.get_channel(starting['samo_jedzonko'])
bot_test = client.get_channel(starting['bot_test'])


me = starting['me']

trash = Garbagson()

allegros = Allegro_scrapping()

@client.event

async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    # print(f'{username}: {user_message}({channel})')
#ponizej ladujemy sobie plik z memami
    #fileNameArray = [x for x in os.listdir("E:/memowo") if os.path.isfile(os.path.join("E:/memowo", x))]
    fileNameArray = [x for x in os.listdir("./memowo") if os.path.isfile(os.path.join("./memowo", x))]
    #print(fileNameArray)
   # "C:/programowanko/memowo"
    

    if message.author == client.user:  #bot nie odpowiada sam sobie
        return


    
    if user_message.lower() == 'test':
        await jarkendar.send('testowa wiadomość wywoływana wszędzie?')


        

    if message.channel.name == 'testy-bot':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(10000)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!pancerniaki':
        await message.channel.send(scrap.pancernioki())

    if user_message.lower() == '!anywhere':
        await message.channel.send('this can be used anywhere!')
        return
                            

    if user_message.lower() == '!mem':
        plik = random.choice(fileNameArray)
        de_cat = "./memowo/"
        plik2 = de_cat+plik
        await message.channel.send(file=discord.File(plik2))
    elif user_message.lower() == '!apmf':
        await message.channel.send('Maxujesz e generalnie połkujesz z e nie zbliżając się')
        await message.channel.send('Pierwszy item łezka da ci mane na spam. Grasz przede wszystkim bezpiecznie')
        await message.channel.send('wykańczasz ich za pomocą E')
        await message.channel.send('itemy buty skrucone cd jasności umysłu jako druie jako trzecie najlepszy kostur rylai')
        await message.channel.send('Następnie wszystko pod magie i efekty na procentowe zdrowie')
        await message.channel.send('sytuacyjnie ale zawsze dobrze Demoniczny uścisk; Cierpienie Liandrego i w tym momencie masz dmg + 10 max hp')
        await message.channel.send('Potem oczywiście klepsydra. Bardoz fajnie jest puścić E a potem R pięknie wtedy kleją')
        await message.channel.send('Jak już masz Rylai nie musisz tego kombować slowy z dmg sie zrobią')
        await message.channel.send('Uważaj jak się ruszysz to cancelujesz ulta. Czyli puszczasz i patrzysz jak im hp spada')

    testowystr = user_message.lower()

    if ('gdzie spok' in testowystr) or ('hej spok' in testowystr) or ('gdzie jest spok' in testowystr):
        time.sleep(8)
        await message.channel.send('SPOOOOKKKK')
        time.sleep(5)
        await message.channel.send('SPOOOOK KURWA')
        time.sleep(7)
        await message.channel.send('NOOO KURWAA SPOOOK ')
        time.sleep(2)
        await message.channel.send('JAK GO POTRZEBA TO KURWA NIGDY GO NIE MA SPOK ZJEBALES')

    
    if '!spam' in testowystr:
        lista = user_message.split()
        komenda, liczba = lista

        if komenda.lower() == '!spam' :
            for i in range(0,int(liczba)):
                # plik_spam = random.choice([x for x in os.listdir("E:\memowo") if os.path.isfile(os.path.join("E:\memowo", x))])
                plik_spam = random.choice(fileNameArray)
                de_cat_spam ='./memowo/'
                plik2_spam = de_cat_spam+plik_spam
                await message.channel.send(file=discord.File(plik2_spam))
               
    if ('linux' in testowystr) or ('ubuntu' in testowystr) or ('linuks' in testowystr):
        time.sleep(3)
        await message.channel.send('Linux jest darmowy i otwarty gdy twój czas jest gówno warty')
    elif ('tragedia' in testowystr) or ('plegius' in testowystr) or ('sidous' in testowystr) or ('ironia' in testowystr) or ('ironiczny' in testowystr)or ('ironiczne' in testowystr) or ('historia' in testowystr) or ('historię' in testowystr) or ('historią' in testowystr) or ('tragedią' in testowystr) or ('tragedię' in testowystr) or ('historyczny' in testowystr):
        await message.channel.send('Czy słyszałeś kiedyś o tragedii Dartha Plagueisa Mądrego?')
        await message.channel.send(file=discord.File('./specjal/palpatine-emperor.gif'))
        time.sleep(4)
        await message.channel.send('Myślałem, że nie. To nie jest historia, którą opowiedziałby ci Jedi.')
        time.sleep(2)
        await message.channel.send('To legenda Sithów. Darth Plagueis był Mrocznym Lordem Sithów, tak potężnym i tak mądrym, że mógł użyć Mocy, by wpłynąć na midichlorian, by stworzyć życie…')
        time.sleep(2)                           
        await message.channel.send('Miał taką wiedzę o Ciemnej Stronie, że potrafił nawet uchronić tych, na których mu zależało, przed śmiercią.')
        time.sleep(1)
        await message.channel.send('Ciemna strona Mocy jest ścieżką do wielu umiejętności, które niektórzy uważają za nienaturalne.')                           
        time.sleep(1)
        await message.channel.send('Stał się taki potężny…')
        time.sleep(2)
        await message.channel.send(' jedyną rzeczą, której się bał, była utrata mocy, co w końcu oczywiście zrobił.')
        time.sleep(1)
        await message.channel.send('Niestety nauczył swojego ucznia wszystkiego, co wiedział, po czym uczeń zabił go we śnie.')
        time.sleep(3)
        await message.channel.send('Ironiczny. Mógł uratować innych od śmierci, ale nie siebie.')


    if user_message.lower() == '!śmieci':
        await message.channel.send(f'%s\n {trash.trash_time()}' % me)


    if '!asearch' in user_message.lower():
        fraze = user_message.split(',')
        fraze = [elem.strip() for elem in fraze]
        await message.channel.send(allegros.single_search(fraze[1:]))


    if '!forecast' in user_message.lower() and user_message != '!forecast':
        city = user_message.split(',')
        city = [elem.strip() for elem in city]
        try:
            await message.channel.send(weather.requesting(city[1]))
        except:
            await message.channel.send("Nie posiadam takiej miejscowości w swojej bazie")
    elif '!forecast' in user_message.lower() and user_message == '!forecast':
        await message.channel.send(weather.weather_check())

    if user_message.lower() == "!help":
        await message.channel.send(f"{starting['help_base']} \n{starting['help_asearch']} \n{starting['help_forecast']}")




async def daty_godziny ():

    await client.wait_until_ready()

    time.sleep(4)
    jarkendar = client.get_channel(starting['jarkendar'])
    samo_jedzonko = client.get_channel(starting['samo_jedzonko'])
    bot_test = client.get_channel(starting['bot_test'])


    papa = 0
    while not client.is_closed():
        await asyncio.sleep(60)
        papierz = 0

        now = datetime.now()
        dataczas = now.strftime("%d/%m/%Y %H:%M:%S")
        czass = dataczas.split(' ', 2)
        data, godzina = czass
        dane_czas = godzina.split(':', 3)
        godz, minuta, sekunda = dane_czas
        # print((godzina, papierz, czass, godzina, godz, minuta, sekunda))
        if (int(godz) == 21) and (int(minuta) == 37) and papa == 0:
            pull = random.randint(1, 2)
            papa = 1
            if pull == 1:
                await samo_jedzonko.send('Przecież to moja ulubioona godzinka')
                await samo_jedzonko.send(file=discord.File('./specjal/papiez-anime.gif'))
            elif pull == 2:
                await samo_jedzonko.send('KTO ŚMIE SZKALOWAĆ PAPIERZAAA !!!!!!')
                await samo_jedzonko.send(file=discord.File('./specjal/papanani.jpg'))
                time.sleep(1)
                await samo_jedzonko.send('OOO Papierzu Boże Imperatorze przybądź !!!!')
                time.sleep(3)
                await samo_jedzonko.send(file=discord.File('./specjal/papemperor1.jpg'))


        elif int(godz)==21 and int(minuta)==38:
            papa = 0

        if (int(godz) == 12 and int(minuta) == 0) or (int(godz) == 20 and int(minuta) == 0):
            await jarkendar.send(f'%s\n {trash.trash_time()}' % me)

        if int(godz) == 6 and int(minuta) == 0:
            await bot_test.send(weather.weather_check())

        if int(godz) == 4 and int(minuta) == 50:
            await jarkendar.send(weather.requesting(starting['home']))
            await jarkendar.send(weather.requesting(starting['work']))

client.loop.create_task(daty_godziny())

client.run(TOKEN)

