import datetime as dt
import pandas as pd
from datetime import timedelta


garbage_df = pd.read_csv("garbage.csv")
# print(garbage_df)
garbage_df['Plastiki'] = pd.to_datetime(garbage_df['Plastiki'], dayfirst=True)
garbage_df['Mieszane'] = pd.to_datetime(garbage_df['Mieszane'], dayfirst=True)
garbage_df['Bio'] = pd.to_datetime(garbage_df['Bio'], dayfirst=True)
garbage_df['Szklo'] = pd.to_datetime(garbage_df['Szklo'], dayfirst=True)
garbage_df['Gabaryty'] = pd.to_datetime(garbage_df['Gabaryty'], dayfirst=True)
garbage_df['Popiol'] = pd.to_datetime(garbage_df['Popiol'], dayfirst=True)

print(garbage_df)
plastiki_df = pd.DataFrame()
plastiki_df['plastiki'] = garbage_df['Plastiki']

mieszane_df = pd.DataFrame()
mieszane_df['mieszane'] = garbage_df['Mieszane']

bio_df = pd.DataFrame()
bio_df['bio'] = garbage_df['Bio']

szklo_df = pd.DataFrame()
szklo_df['szklo'] = garbage_df['Szklo']

gabaryt_df = pd.DataFrame()
gabaryt_df['gabaryt'] = garbage_df["Gabaryty"]

popiol_df = pd.DataFrame()
popiol_df['popiol'] = garbage_df['Popiol']


date = dt.date.today()
future = date + timedelta(days=7)
print(f'current date is: {date}')


# print(f"plastiki : {plastiki_df.head()}  ")
future = future.strftime("%d/%m/%Y")

date = date.strftime("%d/%m/%Y")

message = 'Upcoming trash : \n '

matching_plastik_df =plastiki_df[(plastiki_df.plastiki >= pd.to_datetime(date, dayfirst=True)) &
                                 (plastiki_df.plastiki <= pd.to_datetime(future, dayfirst=True))]

if not matching_plastik_df.empty:
    message += f"Plastiki {matching_plastik_df.plastiki.dt.strftime('%d-%m-%Y').values[0]} " \
               f" it's: {(matching_plastik_df.plastiki.dt.day_name().values[0])} \n"

# print(f'pasujące {matching_plastik_df}')
# matching_plastik_df = matching_plastik_df[(plastiki_df.plastiki <= pd.to_datetime(future, dayfirst=True))]

matching_mieszane_df = mieszane_df[(mieszane_df.mieszane >= pd.to_datetime(date, dayfirst=True)) &
                                   (mieszane_df.mieszane <= pd.to_datetime(future, dayfirst=True))]
if not matching_mieszane_df.empty:
    message += f"Mieszane {matching_mieszane_df.mieszane.dt.strftime('%d-%m-%Y').values[0]} " \
               f"it's: {matching_mieszane_df.mieszane.dt.day_name().values[0]} \n"



matching_bio_df = bio_df[(bio_df.bio >= pd.to_datetime(date, dayfirst=True)) &
                         (bio_df.bio <= pd.to_datetime(future, dayfirst=True))]

if not matching_bio_df.empty:
    message += f"Bio {matching_bio_df.bio.dt.strftime('%d-%m-%Y').values[0]} " \
               f"it's: {matching_bio_df.bio.dt.day_name().values[0]} \n"


matching_szklo_df = szklo_df[(szklo_df.szklo >= pd.to_datetime(date, dayfirst=True)) &
                             (szklo_df.szklo <= pd.to_datetime(future, dayfirst=True))]

if not matching_szklo_df.empty:
    message += f"Szkło {matching_szklo_df.szklo.dt.strftime('%d-%m-%Y').values[0]} " \
               f"it's: {matching_szklo_df.szklo.dt.day_name().values[0]} \n"


matching_gabaryty_df = gabaryt_df[(gabaryt_df.gabaryt >= pd.to_datetime(date, dayfirst=True)) &
                                  (gabaryt_df.gabaryt <= pd.to_datetime(future, dayfirst=True))]
if not matching_gabaryty_df.empty:
    message += f"Gabaryty {matching_gabaryty_df.gabatyt.dt.strftime('%d-%m-%Y').values[0]}" \
               f"it's: {matching_gabaryty_df.gabaryty.dt.day_name().values[0]} \n"

matching_popiol_df = popiol_df[(popiol_df.popiol >= pd.to_datetime(date, dayfirst=True)) &
                              (popiol_df.popiol <= pd.to_datetime(future, dayfirst=True))]

if not matching_popiol_df.empty:
    message += f"Popiół {matching_popiol_df.popiol.dt.strftime('%d-%m-%Y').values[0]} " \
               f"it's: {matching_popiol_df.popiol.dt.day_name().values[0]} \n"



print(f'pasujące {matching_plastik_df.plastiki.dt.day_name()} \n {matching_mieszane_df.mieszane.dt.strftime("%Y-%m-%d").values} \n {matching_gabaryty_df}')

print(message)



matching_garbage_df = garbage_df[(garbage_df >= pd.to_datetime(date, dayfirst=True))]

matching_garbage_df = matching_garbage_df.to_dict()

print(matching_garbage_df)