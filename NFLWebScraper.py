import random
from requests import get
from bs4 import BeautifulSoup

url = "https://www.pro-football-reference.com/years/2018/"
response = get(url)
nfl = BeautifulSoup(response.content, 'html.parser')
teamList = []

afc = nfl.find_all(id='div_AFC')[0].tbody

for tr in afc.find_all('tr'):
    afc_division = tr.find("td", class_="right left")

    if afc_division is not None:
        div = afc_division.text

    afc_team = tr.find('a')

    if afc_team is not None and 'href' in afc_team.attrs:
        afc_name = afc_team.text
        afc_wins = tr.find_all('td')[0].text
        afc_loses = tr.find_all('td')[1].text
        afc_ties = tr.find_all('td')[2].text
        teamList.append(div + ": " +afc_name + " " + afc_wins + "-" + afc_loses + "-" + afc_ties)

nfc = nfl.find_all(id='div_NFC')[0].tbody

for tr2 in nfc.find_all('tr'):
    nfc_division = tr2.find("td", class_="right left")

    if nfc_division is not None:
        div = nfc_division.text

    nfc_team = tr2.find('a')

    if nfc_team is not None and 'href' in nfc_team.attrs:
        nfc_name = nfc_team.text
        nfc_wins = tr2.find_all('td')[0].text
        nfc_loses = tr2.find_all('td')[1].text
        nfc_ties = tr2.find_all('td')[2].text
        teamList.append(div + ": " + nfc_name + " " + nfc_wins + "-" + nfc_loses + "-" + nfc_ties)


print(random.choice(teamList))
