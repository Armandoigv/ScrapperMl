# Funciones de scrapper mercadolibre

from bs4 import BeautifulSoup
import requests
from lxml import etree

def todosProductos(producto):
    lista_titulos = []
    lista_urls = []
    lista_precios = []
    siguiente = 'https://listado.mercadolibre.cl/'+ producto
    print(siguiente)
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
            print("Respondi mal")
            break
        print(pag_ini, pag_fin)
        if pag_ini == pag_fin:
            break
        siguiente = dom.xpath("//div[@class='ui-search-pagination']/ul[1]/li[contains(@class,'--next')]/a")[0].get('href')
    return lista_titulos, lista_urls, lista_precios 

def limite_producto(producto, limite):
    lista_titulos = []
    lista_urls = []
    lista_precios = []
    siguiente = 'https://listado.mercadolibre.cl/'+ producto
    print(siguiente)
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
            print("Respondi mal")
            break
        print(pag_ini, pag_fin)
        if len(lista_titulos) >= int(limite):
            return lista_titulos[:limite], lista_urls[:limite], lista_precios[:limite]

        if pag_ini == pag_fin:
            break
        siguiente = dom.xpath("//div[@class='ui-search-pagination']/ul[1]/li[contains(@class,'--next')]/a")[0].get('href')
    return lista_titulos, lista_urls, lista_precios 