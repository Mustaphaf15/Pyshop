# Generated by Django 4.0.1 on 2022-01-16 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_sites_nb_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='phones',
            name='lien_pub',
            field=models.DateTimeField(null=True, verbose_name="lien de l'annonce"),
        ),
        migrations.AddField(
            model_name='phones',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sites',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sites',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
