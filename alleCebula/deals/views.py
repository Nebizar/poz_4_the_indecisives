from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from deals.models import Item
from deals.models import Comment
from alleCebula.authorization import post_to_page
from django.contrib.auth.decorators import login_required

# get items awarded by community from database - JS will display them
def deals(request):
    template = loader.get_template('deals/index.html')

    products = Item.objects.all()

    context = {
        'products': products
    }
    
    return HttpResponse(template.render(context, request))

def details(request, id):

    if request.method == 'POST':
        print('POSTE')
        com = request.POST.get( 'comment', '')
        name = request.POST.get( 'firstname' , '')

        comment = Comment(
            product_id = Item.objects.get(pk=id),
            content = com,
            nick = name
            )

        comment.save()

    template = loader.get_template('deals/singleSite.html')
    product = Item.objects.get(pk=id)

    comments = Comment.objects.filter(product_id=product)

    context = {
        'product': product,
        'comments': comments
    }

    return HttpResponse(template.render(context, request))

# add cebulion method
def add(request, id):
    product = Item.objects.get(pk=id)
    product.cebulions += 1
    product.save()
    #
    return HttpResponse('')
    #
    
# subtract cebulion method
def sub(request, id):
    product = Item.objects.get(pk=id)
    product.cebulions -= 1
    product.save()
    #
    return HttpResponse('')

@login_required
def post_to_facebook(request, url, msg):
    status = post_to_page(msg+' '+url)
    return HttpResponse('')