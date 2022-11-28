from .models import Kategorie

def menu_links(request):
    links = Kategorie.objects.all()
    return dict(links=links)
