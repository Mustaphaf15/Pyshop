import threading
import time

import requests
from bs4 import BeautifulSoup

from phones.models import Phones
from django.templatetags.static import static


class Scrappers:
    def __init__(self,
                 nomsite,
                 lien,
                 selector_block,
                 selector_img,
                 selector_titre,
                 selector_prix,
                 selector_ville,
                 selector_date_pub,
                 selector_lien):
        self.nomsite = nomsite
        self.lien = lien
        self.selector_block = selector_block
        self.selector_img = selector_img
        self.selector_titre = selector_titre
        self.selector_prix = selector_prix
        self.selector_ville = selector_ville
        self.selector_date_pub = selector_date_pub
        self.selector_lien = selector_lien

    def scrap(self):
        page = requests.get(self.lien)
        soup = BeautifulSoup(page.content, 'lxml')
        items = soup.select(self.selector_block)
        for item in items:
            if not item.select_one(self.selector_prix) is None:
                phone = Phones()
                phone.site = self.nomsite
                phone.titre = item.select_one(self.selector_titre).get_text(strip=True)
                phone.prix = float(
                    "".join(item.select_one(self.selector_prix).get_text(strip=True).replace('DH', '').split()))
                phone.ville = item.select_one(self.selector_ville).get_text(strip=True)
                if not item.select_one(self.selector_img) is None:
                    if 'https://' in item.select_one(self.selector_img)['data-original']:
                        phone.image = item.select_one(self.selector_img)['data-original']
                    else:
                        phone.image = "/".join(self.lien.split("/")[0:3]) + '/'
                        phone.image += item.select_one(self.selector_img)['data-original']

                else:
                    phone.image = static('/img/phone.png')
                if not item.select_one(self.selector_lien) is None:
                    if 'https://' in item.select_one(self.selector_lien)['href']:
                        phone.lien_pub = item.select_one(self.selector_lien)['href']
                    else:
                        phone.lien_pub = "/".join(self.lien.split("/")[0:3]) + '/'
                        phone.lien_pub += item.select_one(self.selector_lien)['href']
                phone.date_pub = item.select_one(self.selector_date_pub).get_text(strip=True)

                if not Phones.objects.filter(titre=phone.titre).exists():
                    phone.save()

        #mise ne pause du webscrapping pendant 5 minutes
        #time.sleep(300)
