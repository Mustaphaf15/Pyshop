from django.db import models


class Sites(models.Model):
    nom_site = models.CharField(max_length=50)
    lien_page = models.URLField(verbose_name="lien d'une page sans numéro", max_length=255)
    nb_page = models.IntegerField(verbose_name="Nb de page à scraper")
    selector_block = models.CharField(verbose_name="Selecteur CSS du block d'annonce", max_length=25)
    selector_img = models.CharField(verbose_name="Selecteur CSS d'image", max_length=25)
    selector_titre = models.CharField(verbose_name="Selecteur CSS du titre", max_length=25)
    selector_prix = models.CharField(verbose_name="Selecteur CSS du prix", max_length=25)
    selector_ville = models.CharField(verbose_name="Selecteur CSS de la ville", max_length=25)
    selector_date_pub = models.CharField(verbose_name="Selecteur CSS de la date de publication", max_length=25)
    selector_lien = models.CharField(verbose_name="Selecteur CSS du lien de la publication", max_length=25)
    create_at = models.DateTimeField(verbose_name="Date  de creation", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Date  de la derniere MAJ", auto_now=True)

    def __str__(self):
        return self.nom_site

    class Meta:
        verbose_name = "Site de vente des smartphones"
        verbose_name_plural = "Site de vente des smartphones"


class Phones(models.Model):
    site = models.ForeignKey(Sites, on_delete=models.CASCADE)
    image = models.URLField(verbose_name="lien photos de l'annonce",max_length=255)
    titre = models.CharField(max_length=255)
    prix = models.FloatField(blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    date_pub = models.CharField(verbose_name="Date  de publication", max_length=100, null=True)
    lien_pub = models.URLField(verbose_name="lien de l'annonce", unique=True)
    create_at = models.DateTimeField(verbose_name="Date  de creation", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Date  de la derniere MAJ", auto_now=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Annonce de vente pour smartphone"
        verbose_name_plural = "Annonces de vente pour smartphone"
