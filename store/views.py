from django.shortcuts import render, get_object_or_404
from .models import product, Kategorie

# Create your views here.
def store(request, kategorie_slug=None):
    Kategorien = None
    products = None

    if kategorie_slug != None:
        Kategorien = get_object_or_404(Kategorie, slug=kategorie_slug)
        products = product.objects.filter(kategorie=Kategorien, is_available=True)
        product_count = products.count()
    else:
        products = product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products' : products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, kategorie_slug, product_slug):
    try:
        single_product = product.objects.get(kategorie__slug=kategorie_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product' : single_product,
    }
    return render(request, 'store/product_detail.html',context)
