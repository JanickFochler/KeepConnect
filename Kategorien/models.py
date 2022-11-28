from django.db import models
from django.urls import reverse

# Create your models here.

class Kategorie(models.Model):
    kategorie_name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=100, unique=True)
    beschreibung = models.CharField(max_length = 255, blank = True)
    kat_image = models.ImageField(upload_to='photos/kategorien', blank=True)

    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


    def __str__(self):
        return self.kategorie_name
