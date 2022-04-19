from bs4 import BeautifulSoup
import requests
from lxml import etree
import pandas as pd

# request1 = requests.get("https://listado.mercadolibre.cl/xiaomi")

# print(request1.status_code)

# soup = BeautifulSoup(request1.content, "html.parser")

# Titulos

# nombres = soup.find_all('h2', attrs={'class':'ui-search-item__title'})

# print(nombres)

# lista_nombres = [i.text for i in nombres]

# print(lista_nombres)

# URLS

# urls = soup.find_all('a', attrs={'class':'ui-search-item__group__element ui-search-link'})

# #print(urls)

# # urls[0].get('href')

# urls = [i.get('href') for i in urls]

# print(urls)

# Declarar dom

# dom = etree.HTML(str(soup))

# #print (dom)

# Se ingresa el xpath de los elementos a buscar

# precios = dom.xpath("//li[@class = 'ui-search-layout__item']//div[@class='ui-search-result__content-columns']//div[@class='ui-search-result__content-column ui-search-result__content-column--left']/div[1]/div//div[@class='ui-search-price__second-line']//span[@class = 'price-tag-amount']/span[2]")

# El precio de un elemento 

#print(precios[0].text)

# precioslista = [i.text for i in precios]

#print (precioslista)
#print (len(precioslista))

#df = pd.DataFrame({"Título": lista_nombres, "Urls": urls, "Precios": precioslista})

#df.to_csv("csv_Mercadolibre.csv")

#print(df)

#siguiente = dom.xpath("//div[@class='ui-search-pagination']/ul[1]/li[contains(@class,'--next')]/a")[0].get('href')

# pag_ini = soup.find('span', attrs={"class":"andes-pagination__link"}).text
# pag_ini = int(pag_ini)

# pag_fin = soup.find('li', attrs={"class":"andes-pagination__page-count"}).text
# pag_fin = int(pag_fin.split(" ")[1])

# print(pag_ini)
# print(pag_fin)
# print(siguiente)

lista_titulos = []
lista_urls = []
lista_precios = []
siguiente = "https://listado.mercadolibre.cl/xiaomi-10s"

while True:
    requestx = requests.get(siguiente)
    if requestx.status_code ==200:
        soup = BeautifulSoup(requestx.content, "html.parser")
        # Titulos
        nombres = soup.find_all('h2', attrs={'class':'ui-search-item__title'})
        nombres = [i.text for i in nombres]
        lista_titulos.extend(nombres)
        # Urls
        urls = soup.find_all('a', attrs={'class':'ui-search-item__group__element ui-search-link'})
        urls = [i.get('href') for i in urls]
        lista_urls.extend(urls)
        # Precios
        dom = etree.HTML(str(soup))
        precios = dom.xpath("//li[@class = 'ui-search-layout__item']//div[@class='ui-search-result__content-columns']//div[@class='ui-search-result__content-column ui-search-result__content-column--left']/div[1]/div//div[@class='ui-search-price__second-line']//span[@class = 'price-tag-amount']/span[2]")
        precios = [i.text for i in precios]
        lista_precios.extend(precios)
        pag_ini = soup.find('span', attrs={"class":"andes-pagination__link"}).text
        pag_ini = int(pag_ini)
        pag_fin = soup.find('li', attrs={"class":"andes-pagination__page-count"}).text
        pag_fin = int(pag_fin.split(" ")[1])
    else:
        break
    print(pag_ini, pag_fin)
    if pag_ini == pag_fin:
        break
    siguiente = dom.xpath("//div[@class='ui-search-pagination']/ul[1]/li[contains(@class,'--next')]/a")[0].get('href')

print(len(lista_titulos))
print(len(lista_urls))
print(len(lista_precios))

df = pd.DataFrame({"Títulos": lista_titulos, "Urls": lista_urls, "Precios": lista_precios})
print(df)
df.to_csv("csv_Mercadolibre.csv")