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

matching_plastik_df =plastiki_df[(plastiki_df.plastiki >= pd.to_datetime(date, dayfirst=True))]
# print(f'pasujące {matching_plastik_df}')
matching_plastik_df = matching_plastik_df[(plastiki_df.plastiki <= pd.to_datetime(future, dayfirst=True))]

print(f'pasujące {matching_plastik_df}')