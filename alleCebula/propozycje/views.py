from django.shortcuts import render
from propozycje.machineLearning.rules import create_rules, get_associated_categories
from alleCebula.productgetter import get_products_from_category, get_products_from_seller
from propozycje.machineLearning.item_generator import categories_dict
from alleCebula.itemyZosi import bundle_to_array, process_xd
from django.http import HttpResponse
from django.template import loader

def propositions(request):
    template = loader.get_template('propozycje/zero/index.html')
    #TODO zamienic na wlasciwe kategorie
    categories = {'aaa', 'bbb', 'ccc', 'ddd'}

    context = {
        'categories': categories,
    }

    return HttpResponse(template.render(context, request))

def process(request, price, category):
    #get data from API and machine learning stuff
    category="monitory"
    base_price=200
    rules = create_rules()
    associated_categories= get_associated_categories(rules, category)

    items_number = 50
    category_number = len(associated_categories)
    items_per_category = items_number // category_number

    cat_id = categories_dict[category]
    items = get_products_from_category(cat_id, num_products=items_per_category, max_price=base_price)
    bundles=[]
    products = []
    bundles=process_xd(items, associated_categories, base_price, items_per_category)
    print(bundles)

    for item in items:
        seller_id=item["seller"]["id"]

        if item["sellingMode"]["format"]=="BUY_NOW":
            other_price=base_price-float(item["sellingMode"]["price"]["amount"])
            for category in associated_categories:
                cat_id=categories_dict[category]
                other_items = get_products_from_category(cat_id, max_price=other_price, num_products=items_per_category)

                for other_item in other_items:
                    bundle_sample = []
                    bundle_sample.append(item)
                    if other_item["sellingMode"]["format"] == "BUY_NOW":
                        bundle_sample.append(other_item)
                        new_price = other_price - float(other_item["sellingMode"]["price"]["amount"])
                        bundles.append(bundle_sample)
                        products = bundle_to_array(bundle_sample)


    template = loader.get_template('propozycje/zero/productList.html')

    """
    products = [
            {
                'name': 'opona',
                'price': '125 zł',
                'image': 'https://a.allegroimg.com/s1024/01100e/9c869ebe48129822b1605ecd4605'
            },
            {
                'name': 'opona',
                'price': '125 zł',
                'image': 'https://a.allegroimg.com/s1024/01100e/9c869ebe48129822b1605ecd4605'
            },
            {
                'name': 'opona',
                'price': '125 zł',
                'image': 'https://a.allegroimg.com/s1024/01100e/9c869ebe48129822b1605ecd4605'
            }
    ]
    """

    bundle = {
        'id': 'abc',
        'products': products
    }

    bundles = []
    bundles.append(bundle)

    context = {
        'bundles': bundles
    }

    return HttpResponse(template.render(context, request))


def buy(request, id):
    print(id)
    return HttpResponse('')