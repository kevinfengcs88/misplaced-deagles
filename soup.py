from bs4 import BeautifulSoup
import requests

def scrape(site):
    result = requests.get(site)
    print(result.status_code)
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

    print(hashbrown)

def scrape2(site):
    result = requests.get(site)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    data = soup.find('span', class_='num')
    print(data.text)

scrape('https://activeplayer.io/valorant/')



scrape2('https://steamcharts.com/app/730')



# with open('https://activeplayer.io/valorant/') as fp:
#     soup = BeautifulSoup(fp, 'html.parser')

