import json
import datetime as dt
from datetime import datetime, timedelta


current = dt.date.today()
future = current + timedelta(days=7)

with open("garbage.json") as file:
    garbage_dict = json.load(file)


empty = []

plastiki_dt=[]
for elem in garbage_dict['Plastiki']:
    new = datetime.strptime(elem, '%d/%m/%Y')
    plastiki_dt.append(new.date())


mieszane_dt = []
for elem in garbage_dict['Mieszane']:
    new = datetime.strptime(elem, '%d/%m/%Y')
    mieszane_dt.append(new.date())


szklo_dt = []
for elem in garbage_dict['Szklo']:
    new = datetime.strptime(elem, '%d/%m/%Y')
    szklo_dt.append(new.date())


bio_dt = []
for elem in garbage_dict['Bio']:
    new = datetime.strptime(elem, '%d/%m/%Y')
    bio_dt.append(new.date())


gabaryty_dt = []
for elem in garbage_dict['Gabaryty']:
    new = datetime.strptime(elem, '%d/%m/%Y')
    gabaryty_dt.append(new.date())


popioły_dt = []
for elem in garbage_dict['Popioly']:
    new = datetime.strptime(elem, '%d/%m/%Y')
    popioły_dt.append(new.date())



message = 'Upcoming garbage: \n'

matching_gabaryty = [gabaryt for gabaryt in gabaryty_dt if (gabaryt >= current) and (gabaryt <= future)]
if not matching_gabaryty == empty:
    message += f"Gabaryty at: {matching_gabaryty[0].strftime('%A')} full date:" \
               f" {matching_gabaryty[0].strftime('%d-%m-%Y')} \n"

matching_mieszane = [mieszane for mieszane in mieszane_dt if mieszane >= current and mieszane <= future]
if not matching_mieszane == empty:
    message += f"Mieszane at: {matching_mieszane[0].strftime('%A')} full date: " \
               f"{matching_mieszane[0].strftime('%d-%m-%Y')} \n"

matching_popioły = [popiol for popiol in popioły_dt if popiol >= current and popiol <= future]
if not matching_popioły == empty:
    message += f"Popioły at: {matching_popioły[0].strftime('%A')} full date: " \
               f"{matching_popioły[0].strftime('%d-%m-%Y')} \n"


matching_szklo = [glass for glass in szklo_dt if glass >= current and glass <= future]
if not matching_szklo == empty:
    message += f"Szkło at: {matching_popioły[0].strftime('%A')} full date: " \
               f"{matching_popioły[0].strftime('%d-%m-%Y')} \n"




matching_bio = [flower for flower in bio_dt if flower >= current and flower <= future]
if not matching_bio == empty:
    message += f"Bio at: {matching_bio[0].strftime('%A')} full date: " \
               f"{matching_bio[0].strftime('%d-%m-%Y')} \n"




matching_plastiki = [plastik for plastik in plastiki_dt if plastik >= current and plastik <= future]
if not matching_plastiki == empty:
    message += f"Plastiki at: {matching_plastiki[0].strftime('%A')} full date: " \
               f"{matching_plastiki[0].strftime('%d-%m-%Y')} \n"


print(message)