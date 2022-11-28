from django.contrib import admin
from .models import Kategorie
# Register your models here.


class KategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('kategorie_name',)}
    list_display = ('kategorie_name', 'slug')
    
admin.site.register(Kategorie, KategorieAdmin)
