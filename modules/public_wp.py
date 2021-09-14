import requests
from requests_toolbelt import MultipartEncoder
from lxml import html
from modules import variables_data as var
from datetime import datetime
import cloudscraper
from time import sleep
import json


class SkPublic:
    def __init__(self, domain):
        self.domain = domain
        session = requests.Session()
        session.headers = var.user_agent
        data_login = var.data_login
        url = f'https://{self.domain}/wp-login.php'
        while True:
            print('Iniciando Sesion.')
            s = cloudscraper.create_scraper(sess=session)
            r = s.post(url, data=data_login)
            if r.status_code == 200:
                break
            else:
                sleep(5)
        self.s = s
