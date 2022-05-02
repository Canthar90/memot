import os
import random

import time
import logging
from datetime import datetime
import discord
from discord import Game
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import json
from scraping import Scrapping, Allegro_scrapping
import asyncio
from datson import Garbagson
from apis import Weather_forecasting
import gc
from discord import FFmpegPCMAudio


with open("starting.json") as start:
    starting = json.load(start)

# TOKEN = 'token'
TOKEN = starting['token']

# client = discord.Client()
client = Bot('!')

scrap = Scrapping()

weather = Weather_forecasting()
paczuchy = client.get_channel(starting["voice_channel"])
logging.basicConfig(level=logging.INFO)


@client.event  # oto element logujacy
async def on_ready():

    logging.info('We are login as {0.user}'.format(client))
    # await paczuchy.connect()









jarkendar = client.get_channel(starting['jarkendar'])
samo_jedzonko = client.get_channel(starting['samo_jedzonko'])
bot_test = client.get_channel(starting['bot_test'])


me = starting['me']

trash = Garbagson()

allegros = Allegro_scrapping()

papa = 0

@client.event

async def on_message(ctx):
    """Searching words in phrases"""

    # username = ctx.message.author
    user_message = ctx.content
    channel = ctx.channel.name
    message = ctx



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


        

    # if message.channel.name == 'testy-bot':
    #     if user_message.lower() == 'hello':
    #         await message.channel.send(f'Hello {username}!')
    #         return
    #     elif user_message.lower() == 'bye':
    #         await message.channel.send(f'See you later {username}!')
    #         return
    #     elif user_message.lower() == '!random':
    #         response = f'This is your random number: {random.randrange(10000)}'
    #         await message.channel.send(response)
    #         return

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
            if int(liczba) > 10:
                await message.channel.send("Paaanie nie szalej pan")
            else:
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

    global papa
    if papa == 1 and ctx.voice_client and message.author == client.user:
        papa = 0
        sound = FFmpegPCMAudio(starting["shadow_sound1"])
        await ctx.guild.voice_client.play(sound)





    await client.process_commands(message)


@client.command(pass_context=True)
async def test(ctx):
    """testing discord famework"""
    await ctx.send("testujemy")

@client.command(pass_context=True)
async def join(ctx):
    """Joining the voice channel"""
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect(reconnect=False)


    else:
        await ctx.send("Panie najpierw rusz dupe i dołącz do kanału głosowego")


@client.command(pass_context=True)
async def stop(ctx):
    """Stops music that bot is playing"""
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.stop()
    else:
        await ctx.send("Panie kochany ja obecnie nic nie gram")


@client.command(pass_context=True)
async def pause(ctx):
    """Pause music that bot is playing"""
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Panie ja obecnie nic nie gram")


@client.command(pass_contxt=True)
async def resume(ctx):
    """Resume music if bot is playing"""
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Panie ja nic nie mam zapałzowanego")


@client.command(pass_context=True)
async def narod(ctx):
    """Plays on of the more controvelsial music pieces in polish culture"""
    if (ctx.voice_client):
        source = FFmpegPCMAudio(starting['shadow_sound2'])
        await ctx.guild.voice_client.play(source)

@client.command(pass_context=True)
async def anthem1(ctx):
    """Plays one of the deamed anthems"""
    if (ctx.voice_client):
        source = FFmpegPCMAudio(starting['shadow_anthem1'])
        await ctx.guild.voice_client.play(source)



@client.command(pass_context=True)
async def leave(ctx):
    """leaving the voice channel"""
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()

@client.command(pass_context=True)
async def showid(ctx):
    """Shows author id"""

    global paczuchy, starting
    channel = paczuchy.voice.channel
    await ctx.channel.send(f"testujemy wiadomości {ctx.author.id}")
    # await channel.connect(reconnect=False)



async def daty_godziny ():
    """Managing time related events"""

    await client.wait_until_ready()

    time.sleep(4)
    jarkendar = client.get_channel(starting['jarkendar'])
    samo_jedzonko = client.get_channel(starting['samo_jedzonko'])
    bot_test = client.get_channel(starting['bot_test'])


    global papa
    while not client.is_closed():
        await asyncio.sleep(59)


        now = datetime.now()
        dataczas = now.strftime("%d/%m/%Y %H:%M:%S")
        czass = dataczas.split(' ', 2)
        data, godzina = czass
        dane_czas = godzina.split(':', 3)
        godz, minuta, sekunda = dane_czas

        if (int(godz) == 21) and (int(minuta) == 37) and papa == 0:
            pull = random.randint(1, 2)
            papa = 1
            if pull == 1:
                # @client.event
                # async def on_message(ctx):
                #     sound = FFmpegPCMAudio(starting["shadow_sound1"])
                #     await ctx.guild.voice_client.play(sound)
                await samo_jedzonko.send('Przecież to moja ulubioona godzinka')
                await samo_jedzonko.send(file=discord.File('./specjal/papiez-anime.gif'))


            elif pull == 2:
                # @client.event
                # async def on_message(ctx):
                #     sound = FFmpegPCMAudio(starting["shadow_sound1"])
                #     await ctx.guild.voice_client.play(sound)
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


        if int(godz) == 3 and int(minuta) == 50:
            await jarkendar.send(weather.requesting(starting['home']))
            await jarkendar.send(weather.requesting(starting['work']))

client.loop.create_task(daty_godziny())

client.run(TOKEN)

