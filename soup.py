from bs4 import BeautifulSoup
import requests

def scrape_activeplayer_val():
    result = requests.get('https://activeplayer.io/valorant/')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    table = soup.table
    table_rows = table.find_all('tr')
    hashbrown = {}

    flag = True
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if flag:
            flag = False
            continue
        hashbrown[row[0]] = row[1]

    count = int(hashbrown['Online Players (1H)'].replace(',', ''))
    print('Number of concurrent Valorant players (activeplayer.io):')
    print(count)

def scrape_steamcharts_csgo():
    result = requests.get('https://steamcharts.com/app/730')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    data = soup.find('span', class_='num')
    count = int(data.text)
    print('Number of concurrent CSGO players: ')
    print(count)

def scrape_player_counter_val():
    result = requests.get('https://playercounter.com/valorant/')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    data = soup.find('h2')
    count = int(data.text.split(' ')[0].replace(',', '')) 
    print('Number of concurrent Valorant players (playercounter):')
    print(count)

scrape_activeplayer_val()
scrape_steamcharts_csgo()
scrape_player_counter_val()
