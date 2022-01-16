from django.contrib import admin

from phones.models import Sites, Phones


@admin.register(Sites)
class SitesscrapAdmin(admin.ModelAdmin):
    list_display = ('nom_site',
                    'lien_page',
                    'nb_page',
                    'create_at',
                    'update_at',)


@admin.register(Phones)
class PhonesscrapAdmin(admin.ModelAdmin):
    list_display = ('site',
                    'titre',
                    'prix',
                    'ville',
                    'create_at',
                    'update_at',)
    list_filter = ('site',
                    'titre',
                    'prix',
                    'ville',
                    'create_at',)