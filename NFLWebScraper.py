import random
from requests import get
from bs4 import BeautifulSoup

# Set target URL and parse HTML page content
url = "https://www.pro-football-reference.com/years/2018/"
response = get(url)
nfl = BeautifulSoup(response.content, 'html.parser')
teamList = []

# Find the HTML div for the AFC standings section
afc = nfl.find_all(id='div_AFC')[0].tbody

# Iterate through all table rows
for tr in afc.find_all('tr'):
    # Find table row with specific detail name
    afc_division = tr.find("td", class_="right left")

    # Validate the value is not a NoneType to avoid errors
    if afc_division is not None:
        div = afc_division.text

    # Find the rows with team hyper links
    afc_team = tr.find('a')

    # Validate the value is not a NoneType to avoid errors and has a valid hyperlink value
    if afc_team is not None and 'href' in afc_team.attrs:
        # Parse desired values from table row and add to list
        afc_name = afc_team.text
        afc_wins = tr.find_all('td')[0].text
        afc_loses = tr.find_all('td')[1].text
        afc_ties = tr.find_all('td')[2].text
        teamList.append(div + ": " +afc_name + " " + afc_wins + "-" + afc_loses + "-" + afc_ties)

# Find the HTML div for the NFC standings section
nfc = nfl.find_all(id='div_NFC')[0].tbody

# Iterate through all table rows
for tr2 in nfc.find_all('tr'):
    # Find table row with specific detail name
    nfc_division = tr2.find("td", class_="right left")

    # Validate the value is not a NoneType to avoid errors
    if nfc_division is not None:
        div = nfc_division.text

    # Find the rows with team links
    nfc_team = tr2.find('a')

    # Validate the value is not a NoneType to avoid errors and has a valid hyperlink value
    if nfc_team is not None and 'href' in nfc_team.attrs:
        # Parse desired values from table row and add to list
        nfc_name = nfc_team.text
        nfc_wins = tr2.find_all('td')[0].text
        nfc_loses = tr2.find_all('td')[1].text
        nfc_ties = tr2.find_all('td')[2].text
        teamList.append(div + ": " + nfc_name + " " + nfc_wins + "-" + nfc_loses + "-" + nfc_ties)

# Print out a random team from list
print(random.choice(teamList))
