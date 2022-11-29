
from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name="store"),
    path('kategorie/<slug:kategorie_slug>/', views.store, name='products_by_category'),
    path('<slug:kategorie_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
]
