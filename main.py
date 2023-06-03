from soup import *
import pandas as pd
import os.path
import csv

val_count = scrape_player_counter_val()
csgo_count = scrape_steamcharts_csgo()

path = 'data/population.csv'

new_data = str(val_count) + ',' + str(csgo_count)

with open(path, 'a') as f:
    if os.path.getsize(path) == 0:
        pass
    else:
        f.write('\n')
    f.write(new_data)

print('====================')
print('After:')
df = pd.read_csv(path, header=None)
print(df)
