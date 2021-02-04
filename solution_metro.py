# Trouver tous les tags: table, tr, td  dans le site web suivant
# url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
# Puis pour retourner tous les noms des stations de metros et leurs numeros de ligne associes.
# Choisir son format de donnees


from bs4 import BeautifulSoup
import requests

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find('table')

data = []

for tr in table.findAll('tr'):
    index = 0
    station = ""
    lignes = []
    for td in tr.findAll('td')[::3]:
        for a in td.findAll('a'):
            if index == 0:
                station = a.text
                print(station)
            else:
                lignes.append(a.text)
                print(lignes)
        index += 1
    data.append([station, lignes])

print(data)