# Generated by Django 4.1.3 on 2022-11-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kategorien', '0002_alter_kategorie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorie',
            name='kat_image',
            field=models.ImageField(blank=True, upload_to='photos/kategorien'),
        ),
    ]
