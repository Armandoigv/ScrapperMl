from bs4 import BeautifulSoup
import requests

# Importar modulo etree

from lxml import etree

req1 = requests.get("https://pokemondb.net/pokedex/all")

print(req1.status_code)

soup = BeautifulSoup(req1.content, "html.parser")

#print (soup)

# Declarar dom

dom = etree.HTML(str(soup))

#print (dom)

# Se ingresa el xpath de los elementos a buscar

nombres = dom.xpath("//table[@id = 'pokedex']/tbody/tr/td[@class='cell-name']/a")

# El nombre de un elemento 

#print(nombres[0].text)

nombreslista = [i.text for i in nombres]

print (nombreslista)
print (len(nombreslista))
