"""Importamos las librerias que vamos a usar"""
from openpyxl import Workbook
from bs4 import BeautifulSoup
import requests
import pandas as pd

"""Primero vamos a conseguir la URL del sitio que queremos sacar la informacion"""

url ="https://coinmarketcap.com/es/all/views/all/"

"""Descargamos el contenido de la pagina"""

page = requests.get(url)

"""Transformamos a formato BeautifulSoup"""

soup = BeautifulSoup(page.content , "html.parser")

#Monedas
"""Definimos de donde extraer los datos"""

M = soup.find_all("a" , class_="cmc-table__column-name--name cmc-link" )

monedas = list()

contador = 0

"""Guardamos los datos filtrados en la lista monedas"""

for i in M:
    if contador < 10:
        monedas.append(i.text)
    else:
        break
    contador += 1
    
"""Creamos una lista que cuenta del 1 al 10 para el ranking"""

rank = list()

for i in range(10):
    rank.append(i+1)
    


"""Creamos el DataFrame"""

df = pd.DataFrame({"Ranking" : rank,"Moneda" : monedas})


"""Para finalizar lo exportamos a formato xlsx para ser leido por un excel"""

df.to_excel("Ranking_Crypto.xlsx", index=False)
