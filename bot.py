import os
import random
import time
import logging
from datetime import datetime
import discord
from discord.ext.commands import Bot
import json
from scraping import Scrapping, Allegro_scrapping
import asyncio
from datson import Garbagson, Events, CyclicEvents
from apis import Weather_forecasting, RandoCatApi, LOTRapi, JokeApi, CurrencyApi, DrinkApi
from discord import FFmpegPCMAudio


with open("starting.json") as start:
    starting = json.load(start)

queues = {}


def check_queue(ctx, channel_id):
    if queues:
        if queues[channel_id]:
            voice = ctx.guild.voice_client
            source = queues[channel_id].pop(0)
            player = voice.play(source, after=lambda x=None: check_queue(ctx, channel_id))


async def play_thing(ctx, song_id):
    """Plays passed song if bot is placed in voice channel"""
    if ctx.voice_client:
        source = FFmpegPCMAudio(starting[song_id])
        await ctx.guild.voice_client.play(source)


async def queueing(ctx, *args):
    """Adding items to queue"""
    for arg in args:
        voice = ctx.guild.voice_client
        song = starting[arg]
        source = FFmpegPCMAudio(song)
        guild_id = ctx.message.guild.id

        if guild_id in queues:
            queues[guild_id].append(source)
        else:
            queues[guild_id] = [source]
    await ctx.send("Added to queue")

TOKEN = starting['token']

client = Bot('!')

scrap = Scrapping()

drink_api = DrinkApi()
currency_api = CurrencyApi()
joke_api = JokeApi()
lotr_api = LOTRapi()
cat_api = RandoCatApi()
weather = Weather_forecasting()
paczuchy = client.get_channel(starting["voice_channel"])
logging.basicConfig(level=logging.INFO)
greviouses_path = "./specjal/grevious special"
greviouses = [x for x in os.listdir(greviouses_path) if os.path.isfile(os.path.join(greviouses_path, x))]


@client.event
async def on_ready():

    logging.info('We are login as {0.user}'.format(client))


jarkendar = client.get_channel(starting['jarkendar'])
samo_jedzonko = client.get_channel(starting['samo_jedzonko'])
bot_test = client.get_channel(starting['bot_test'])

events = Events()

cyclic = CyclicEvents()

me = starting['me']
trash = Garbagson()
allegros = Allegro_scrapping()
papa = 0

fileNameArray = [x for x in os.listdir("./memowo") if os.path.isfile(os.path.join("./memowo", x))]


@client.event
async def on_message(ctx):
    """Searching words in phrases"""

    user_message = ctx.content
    channel = ctx.channel.name
    message = ctx

    global papa
    if message.author == client.user and not papa == 1:
        return

    testowystr = user_message.lower()

    if ('linux' in testowystr) or ('ubuntu' in testowystr) or ('linuks' in testowystr):
        time.sleep(3)
        await message.channel.send('Linux jest darmowy i otwarty gdy tw??j czas jest g??wno warty')
    elif ('tragedia' in testowystr) or ('plegius' in testowystr) or ('sidous' in testowystr) or ('ironia' in testowystr) or ('ironiczny' in testowystr)or ('ironiczne' in testowystr) or ('historia' in testowystr) or ('histori??' in testowystr) or ('histori??' in testowystr) or ('tragedi??' in testowystr) or ('tragedi??' in testowystr) or ('historyczny' in testowystr):
        await message.channel.send('Czy s??ysza??e?? kiedy?? o tragedii Dartha Plagueisa M??drego?')
        await message.channel.send(file=discord.File('./specjal/palpatine-emperor.gif'))
        time.sleep(4)
        await message.channel.send('My??la??em, ??e nie. To nie jest historia, kt??r?? opowiedzia??by ci Jedi.')
        time.sleep(2)
        await message.channel.send('To legenda Sith??w. Darth Plagueis by?? Mrocznym Lordem Sith??w, tak pot????nym i tak m??drym, ??e m??g?? u??y?? Mocy, by wp??yn???? na midichlorian, by stworzy?? ??ycie???')
        time.sleep(2)                           
        await message.channel.send('Mia?? tak?? wiedz?? o Ciemnej Stronie, ??e potrafi?? nawet uchroni?? tych, na kt??rych mu zale??a??o, przed ??mierci??.')
        time.sleep(1)
        await message.channel.send('Ciemna strona Mocy jest ??cie??k?? do wielu umiej??tno??ci, kt??re niekt??rzy uwa??aj?? za nienaturalne.')                           
        time.sleep(1)
        await message.channel.send('Sta?? si?? taki pot????ny???')
        time.sleep(2)
        await message.channel.send(' jedyn?? rzecz??, kt??rej si?? ba??, by??a utrata mocy, co w ko??cu oczywi??cie zrobi??.')
        time.sleep(1)
        await message.channel.send('Niestety nauczy?? swojego ucznia wszystkiego, co wiedzia??, po czym ucze?? zabi?? go we ??nie.')
        time.sleep(3)
        await message.channel.send('Ironiczny. M??g?? uratowa?? innych od ??mierci, ale nie siebie.')

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
            await message.channel.send("Nie posiadam takiej miejscowo??ci w swojej bazie")
    elif '!forecast' in user_message.lower() and user_message == '!forecast':
        await message.channel.send(weather.weather_check())

    if papa == 1 and message.author == client.user:
        if ctx.guild.voice_client:
            ctx.guild.voice_client.stop()
            papa = 0
            sound = FFmpegPCMAudio(starting["barka"])
            await ctx.guild.voice_client.play(sound)

    if "hello there" in user_message.lower() or "lightsaber" in user_message.lower():
        grevious = random.choice(greviouses)
        path_base = "./specjal/grevious special/"
        grevious_path = path_base + grevious
        await ctx.channel.send(file=discord.File(grevious_path))

    await client.process_commands(message)


@client.command(pass_context=True)
async def mem(ctx):
    """Sends one random meme"""
    file_part = random.choice(fileNameArray)
    base = "./memowo/"
    file_final = base + file_part
    await ctx.send(file=discord.File(file_final))


@client.command(pass_context=True)
async def spam(ctx, number):
    """Sending number of memes, max number 10"""
    if int(number) <= 10:
        for i in range(0, int(number)):
            file_part = random.choice(fileNameArray)
            base = "./memowo/"
            file_final = base + file_part
            await ctx.send(file=discord.File(file_final))


@client.command(pass_context=True)
async def pancerniaki(ctx):
    """checks dates of 5 next seances of 4 pancerni i pies in polish television"""
    await ctx.send(scrap.pancernioki())


@client.command(pass_context=True)
async def garbage(ctx):
    """checks if there is any garbage upcoming in next 7 days"""
    await ctx.send(f'%s\n {trash.trash_time()}' % me)


@client.command(pass_context=True)
async def test(ctx):
    """testing discord famework"""
    await ctx.send("testujemy")


@client.command(pass_context=True)
async def join(ctx):
    """Joining the voice channel"""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect(reconnect=False)
    else:
        await ctx.send("Panie najpierw rusz dupe i do????cz do kana??u g??osowego")


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
        await ctx.send("Panie ja nic nie mam zapa??zowanego")


@client.command(pass_context=True)
async def gaz(ctx):
    """Plays legendary polish discopolo music about fast cars"""
    await play_thing(ctx=ctx, song_id="gaz")


@client.command(pass_context=True)
async def soap(ctx):
    """Plays legendary polish song about some soap"""
    await play_thing(ctx=ctx, song_id="soap")


@client.command(pass_context=True)
async def faast(ctx):
    """Plays gonna go fast theme"""
    await play_thing(ctx=ctx, song_id="faast")


@client.command(pass_context=True)
async def hess(ctx):
    """Plays song in honor of some guy"""
    await play_thing(ctx=ctx, song_id="hess")


@client.command(pass_context=True)
async def narod(ctx):
    """Plays on of the more controvelsial music pieces in polish culture"""
    await play_thing(ctx=ctx, song_id="narod")


@client.command(pass_context=True)
async def anthem1(ctx):
    """Plays one of the deamed anthems"""
    await play_thing(ctx=ctx, song_id="anthem1")


@client.command(pass_context=True)
async def anthem2(ctx):
    """Plays second of the deamed anthems"""
    await play_thing(ctx=ctx, song_id="anthem2")


@client.command(pass_context=True)
async def jtheme(ctx):
    """Plays Theme from great cartoon"""
    await play_thing(ctx=ctx, song_id="jtheme")


@client.command(pass_context=True)
async def szanty(ctx):
    """Makes sailors songs playlist"""
    argi = ['bitwa', 'dziewczyny', 'morskieh', "morskie", "keja"]
    await queueing(ctx, *argi)
    check_queue(ctx, ctx.message.guild.id)


@client.command(pass_context=True)
async def play(ctx, arg=''):
    """Plays song by title"""
    if arg == '':
        check_queue(ctx, ctx.message.guild.id)
    else:
        voice = ctx.guild.voice_client
        song = starting[arg]
        source = FFmpegPCMAudio(song)
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))


@client.command(pass_context=True)
async def queue(ctx, *args):
    """adding song to queue"""
    argi = list(args)
    await queueing(ctx, *argi)


@client.command(pass_context=True)
async def leave(ctx):
    """leaving the voice channel"""
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()


@client.command(pass_context=True)
async def add_event(ctx, date, *args):
    """Adding custom event from events class date format YYYY-MM-DD description"""
    try:
        date_test = datetime.strptime(date, "%Y-%m-%d").date()
        title = ' '.join(args)
        channel = ctx.channel.id
        await ctx.channel.send(events.add_event(date=date, title=title, channel=channel))
    except:
        await ctx.channel.send("You typed wrong data expected format is YYYY-MM-DD multi word description")


@client.command(pass_context=True)
async def check_events(ctx):
    """Checking if there are any event upcoming"""
    flag, mathing_events = events.event_detection()
    if flag:
        for key in mathing_events:
            channel = client.get_channel(mathing_events[key][1])
            date = mathing_events[key][0]
            await channel.send(f"Uwaga!! {key}, o {date}")
    else:
        await ctx.channel.send("nie ma ??adnych nadchodz??cych event??w ")


@client.command(pass_context=True)
async def check_cyclic(ctx):
    """Checks if there are any cyclic events upcoming"""
    flag, mathing_events = cyclic.event_detection()
    if flag:
        for key in mathing_events:
            channel = client.get_channel(mathing_events[key][1])
            date = mathing_events[key][0]
            await channel.send(f"Uwaga!! {key} o {date}")
    else:
        await ctx.channel.send("Nie nadchodz?? ??adne wydarzenia")


@client.command(pass_context=True)
async def add_cyclic(ctx, date, *args):
    """Adds cyclic event like birthday date should be added in format like MM-DD description"""
    try:
        date_test = datetime.strptime(f"{datetime.strftime(datetime.today(), format('%Y'))}-{date}",
                                      format("%Y-%m-%d")).date()
        title = ' '.join(args)
        channel = ctx.channel.id
        await ctx.channel.send(cyclic.add_item(date=date, title=title, channel=channel))
    except:
        await ctx.channel.send("You passed data in wrong format expected format MM-DD multi word description")


@client.command(pass_context=True)
async def kitten(ctx):
    """Gets random citten image"""
    await ctx.channel.send(cat_api.get_random_cat())


@client.command(pass_context=True)
async def lotr_quote(ctx):
    """Gets random lotr quote"""
    await ctx.channel.send(lotr_api.get_random_quote())


@client.command(pass_context=True)
async def joke(ctx):
    """Sends random joke"""
    setup, delivery = joke_api.get_joke()
    await ctx.channel.send(setup)
    if delivery:
        time.sleep(2)
        await ctx.channel.send(delivery)


@client.command(pass_context=True)
async def drink_by_name(ctx, *args):
    """Searches drink by name"""
    question = list(args)
    q = ' '.join(question)
    await ctx.channel.send(drink_api.search_by_name(q))


@client.command(pass_context=True)
async def random_drink(ctx):
    """Searches random drink recipe"""
    await ctx.channel.send(drink_api.random_drink())


@client.command(pass_context=True)
async def drink_by_ingredient(ctx, ingredient):
    """Searches drinks you can do witch given ingredient"""
    drinks_list, flag = drink_api.search_by_ingredient(ingredient=ingredient)
    if flag:
        for drink in drinks_list:
            await ctx.channel.send(drink[0] + "\n" + drink[1])
    else:
        await ctx.channel.send(drinks_list[0])


@client.command(pass_context=True)
async def exchange(ctx, currnency_name, amount=None):
    """Converts given currency in given ammount(optional) to PLN"""
    if type(amount) == str:
        amount = amount.replace(",", ".")
        amount = float(amount)

    if amount != None:
        try:
            await ctx.channel.send(f" Konwersja waluty {currnency_name} dla ilo??ci {amount} na pln to"
                                f" {currency_api.get_custom(currency_name=currnency_name, ammount=amount)} PLN")
        except:
            await ctx.channel.send("Prosz?? poda?? dane w formacie waluta ilo????(opcjonalny) np EUR 5")
    else:
        try:
            await ctx.channel.send(f"Kurs waluty {currnency_name} to "
                                f"{currency_api.get_custom(currency_name=currnency_name)} PLN")
        except:
            await ctx.channel.send("Prosz?? poda?? dane w formacie waluta ilo????(opcjonalny) np EUR 5")


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
        timesdata = now.strftime("%d/%m/%Y %H:%M:%S")
        curr_time = timesdata.split(' ', 2)
        date, clock = curr_time
        dane_czas = clock.split(':', 3)
        houer, minnute, sec = dane_czas

        if (int(houer) == starting['houer']) and (int(minnute) == starting['minutes']) and papa == 0:
            pull = random.randint(1, 2)
            papa = 1
            if pull == 1:
                await samo_jedzonko.send(starting["special_quote1.1"])
                await samo_jedzonko.send(file=discord.File(starting["special_gif"]))
            elif pull == 2:
                await samo_jedzonko.send(starting['special_quote2.1'])
                await samo_jedzonko.send(file=discord.File(starting["special_jpg1"]))
                time.sleep(1)
                await samo_jedzonko.send(starting["special_quote2.2"])
                time.sleep(3)
                await samo_jedzonko.send(file=discord.File(starting["special_jpg2"]))
        elif int(houer) == 21 and int(minnute) == 38:
            papa = 0

        if (int(houer) == 12 and int(minnute) == 0) or (int(houer) == 20 and int(minnute) == 0):
            await jarkendar.send(f'%s\n {trash.trash_time()}' % me)
            flag, mathing_events = events.event_detection()
            if flag:
                for key in mathing_events:
                    channel = client.get_channel(mathing_events[key][1])
                    date = mathing_events[key][0]
                    await channel.send(f"Uwaga!! {key}, o {date}")
            else:
                pass

        if int(houer) == 6 and int(minnute) == 0:
            pass

        if (int(houer) == 3) and (int(minnute) == 50):
            await jarkendar.send(weather.requesting(starting['home']))
            await jarkendar.send(weather.requesting(starting['work']))

client.loop.create_task(daty_godziny())
client.run(TOKEN)

