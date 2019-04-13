from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from deals.models import Item

def deals(request):
    template = loader.get_template('deals/index.html')
    
    """
    pr = Item(
        picture = "https://1.allegroimg.com/s720/0322e5/21cfc7684e40928e4445a5c74751",
        name = "MYSZKA BEZPRZEWODOWA LOGITECH M545 CZARNA",
        price = 95,
        cebulions = "0",
        category_id = "4575"
    )
    pr.save()"""

    products = Item.objects.all()

    context = {
        'products': products
    }
    
    return HttpResponse(template.render(context, request))

def details(request, id):
    template = loader.get_template('deals/singleSite.html')

    product = Item.objects.get(pk=id)

    context = {
        'product': product
    }

    return HttpResponse(template.render(context, request))