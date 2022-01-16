# Generated by Django 4.0.1 on 2022-01-16 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='selector_lien',
            field=models.CharField(default='', max_length=25, verbose_name='Selecteur CSS du lien de la publication'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sites',
            name='selector_block',
            field=models.CharField(max_length=25, verbose_name="Selecteur CSS du block d'annonce"),
        ),
    ]