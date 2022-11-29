from django.shortcuts import render, get_object_or_404
from .models import Product, Kategorie
from carts.models import Cart, CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


# Create your views here.
def store(request, kategorie_slug=None):
    Kategorien = None
    products = None

    if kategorie_slug != None:
        Kategorien = get_object_or_404(Kategorie, slug=kategorie_slug)
        products = Product.objects.filter(kategorie=Kategorien, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products' : paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, kategorie_slug, product_slug):
    try:
        single_product = Product.objects.get(kategorie__slug=kategorie_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()
    
    except Exception as e:
        raise e

    context = {
        'single_product' : single_product,
        'in_cart' : in_cart,
    }
    return render(request, 'store/product_detail.html',context)

def search (request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-create_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)