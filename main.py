from soup import *
import pandas as pd

val_count = scrape_player_counter_val()
csgo_count = scrape_steamcharts_csgo()

print(val_count)
print(csgo_count)

f = open('data/population.csv', 'w')
