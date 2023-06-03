from soup import *
import pandas as pd
import os.path
import csv
from datetime import datetime

val_count = scrape_player_counter_val()
csgo_count = scrape_steamcharts_csgo()

now = datetime.now()
current_month = now.month
current_day = now.day
current_year = now.year
current_hour = now.hour
current = str(current_month) + '/' + str(current_day) + '/' + str(current_year) + '/' + str(current_hour)

new_data = current + ',' + str(val_count) + ',' + str(csgo_count)

path = 'data/population.csv'
with open(path, 'a') as f:
    if os.path.getsize(path) == 0:
        pass
    else:
        f.write('\n')
    f.write(new_data)

print('====================')
print('population.csv:')
df = pd.read_csv(path, header=None)
print(df)
