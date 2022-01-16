import threading

from apscheduler.schedulers.background import BackgroundScheduler

from phones.models import Sites
from phones.webscraping import Scrappers


def startrunner():
    print('startrunner')


def gotoscrap():
    sites = Sites.objects.all()
    for site in sites:
        def runsitescrap():
            i = 0
            while i < site.nb_page:
                scraper = Scrappers(nomsite=site,
                                    lien=site.lien_page + str(i + 1),
                                    selector_block=site.selector_block,
                                    selector_img=site.selector_img,
                                    selector_titre=site.selector_titre,
                                    selector_prix=site.selector_prix,
                                    selector_ville=site.selector_ville,
                                    selector_date_pub=site.selector_date_pub,
                                    selector_lien=site.selector_lien,
                                    )
                scraper.scrap()
                i += 1

        #Si un webscrapping du site est déjà en cours on passe au site suivant:
        runningthreads = [x.name for x in threading.enumerate()]
        if not site in runningthreads:
            threading.Thread(target=runsitescrap(), name=site)