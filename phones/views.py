import csv

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render

from phones.models import Phones
from phones.scraperthread import gotoscrap


def index(request):
    context = {}
    if request.method == 'POST':
        searched = request.POST['searched']
        if len(searched) and searched.strip():
            listedestelephone = Phones.objects.filter(titre__contains=searched).values()
            df = pd.DataFrame(listedestelephone)
            context ['analyse_ville'] = df.groupby('ville').agg({'prix': ['count', 'mean', 'min', 'max']})
            context['messagealerte'] = f"La liste des articles trouver avec:  {searched}!"
            context['typealerte'] = 'info'
            if not listedestelephone.exists():
                listedestelephone = Phones.objects.all().order_by('-id').values()[:30]
                context['messagealerte'] = f"Nous n'avons pas trouvé d'article avec {searched}!"
                context['typealerte'] = 'warning'
        else:
            listedestelephone = Phones.objects.all().order_by('-id').values()[:30]
            context['messagealerte'] = "Vous avez oublié de remplir le champ de recherche !"
            context['typealerte'] = 'danger'
    else:
        listedestelephone = Phones.objects.all().order_by('id').values()[:30]

    context['listedestelephone'] = listedestelephone

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
    gotoscrap()
    listedestelephone = Phones.objects.values()[:30]
    context = {
        'messagealerte': 'Une nouvelle extraction du contenu des sites Web est lancée avec succès!',
        'typealerte': 'success',
        'listedestelephone': listedestelephone,
    }
    response = render(request, 'phones/index.html', context)
    return response

