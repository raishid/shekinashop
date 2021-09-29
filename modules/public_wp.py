import requests
from requests_toolbelt import MultipartEncoder
from lxml import html
from modules import variables_data as var
from datetime import datetime
import cloudscraper
from time import sleep
import json
import csv


class SkPublic:
    def __init__(self, domain):
        self.domain = domain
        session = requests.Session()
        session.headers = var.user_agent_login
        data_login = var.data_login
        url = f'https://{self.domain}/wp-login.php'
        while True:
            print('Iniciando Sesion.')
            s = cloudscraper.create_scraper(sess=session)
            r = s.post(url, data=data_login, allow_redirects=True)
            if r.status_code == 200:
                break
            else:
                sleep(5)
        self.s = s
        self.s.get(f'https://{self.domain}/wp-admin')


    def readData(self, filejson):
        file = open(filejson, 'r', encoding='UTF-8').read()
        data = json.loads(file)
        return data['data']['products']['results']
    """
    "name": titulo,
          "techReport": descripcion corta,
          "externalId": SKU,
          "availableQuantity": stock,
          "description": "descipcion larga",
          "newBasePrice": precio,
          "category": {
            "name": categoria
          },
          "vendor": {
            "businessName": etiqueta
          },
    """
    def PublicProduct(self, data_public):
        titulo = data_public['name']
        desc_corta = data_public['techReport']
        sku = data_public['externalId']
        stock = data_public['availableQuantity']
        desc_larga = data_public['description']
        precio = data_public['newBasePrice']
        categoria = var.categorias[data_public['category']['name']]
        tag = data_public['vendor']['businessName']

        #print(self.s.cookies)
        r = self.s.get(f'https://{self.domain}/wp-admin/post-new.php?post_type=product')
        soup = html.fromstring(r.text)
        wpnonce = soup.xpath('//input[@name="_wpnonce"]/@value')[0]
        print(wpnonce)

    def Leer_csv(self):
        data = list()
        with open('1.csv', 'r', encoding='UTF-8', newline='') as db:
            w = csv.DictReader(db)
            for row in w:
                valores = {
                    'id': row['id'],
                    'descripción_corta': row['descripción_corta'],
                    'SKU': row['SKU'],
                    'name': row['name'],
                    'inventario': row['inventario'],
                    'description': row['description'],
                    'precio': row['precio_normal'],
                    'etiquetas': row['etiquetas'],
                    'categorias': row['categorias'],
                    'image/url': row['image/url'],
                    'images/0/url': row['images/0/url'],
                    'images/1/url': row['images/1/url'],
                    'images/2/url': row['images/2/url'],
                    'images/3/url': row['images/3/url'],
                    'images/4/url': row['images/4/url'],
                    'images/5/url': row['images/5/url'],
                    'images/6/url': row['images/6/url'],
                    'images/7/url': row['images/7/url'],
                    'images/8/url': row['images/8/url'],
                    'images/9/url': row['images/9/url'],
                    'images/10/url': row['images/10/url'],
                    'images/11/url': row['images/11/url'],
                    'images/12/url': row['images/12/url'],
                    'images/13/url': row['images/13/url'],
                    'images/14/url': row['images/14/url'],
                    'images/15/url': row['images/15/url'],
                    'images/16/url': row['images/16/url'],
                    'images/17/url': row['images/17/url'],
                    'images/18/url': row['images/18/url'],
                    'images/19/url': row['images/19/url'],
                    'images/20/url': row['images/20/url'],
                }
                data.append(valores)
            return data
