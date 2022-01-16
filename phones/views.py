import csv

from django.http import HttpResponse
from django.shortcuts import render

from phones.models import Phones
from phones.scraperthread import gotoscrap


def index(request):
    # On démarre le web scrapping en tâche de fond
    gotoscrap

    listedestelephone = Phones.objects.values()[:30]
    context = {
        'listedestelephone': listedestelephone,
    }

    return render(request, 'phones/index.html', context)


def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['titre', 'prix', 'ville', 'date de publication',
                     'lien de la publication'])
    for phone in Phones.objects.all():
        writer.writerow([phone.titre, phone.prix, phone.ville, phone.date_pub, phone.lien_pub])
    response['Content_Disposition'] = 'attachment; filename= "phone.csv"'
    return response

def webscrap(request):
    gotoscrap
    context = {
        'alertescrap': 'webscrapping lancer avec succès!',
    }
    response = render(request, 'phones/index.html', context)
    return response