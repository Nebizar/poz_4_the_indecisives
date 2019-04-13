from django.shortcuts import render
from propozycje.machineLearning.rules import create_rules, get_associated_categories, add_new_data
from alleCebula.productgetter import get_products_from_category, get_products_from_seller
from propozycje.machineLearning.item_generator import categories_dict
from alleCebula.itemyZosi import bundle_to_array, process_xd, shuffle_bundles
from django.http import HttpResponse
from django.template import loader

def propositions(request):
    template = loader.get_template('propozycje/zero/index.html')
    #TODO zamienic na wlasciwe kategorie
    categories = {'myszki','klawiatury','zestaw klawiatura i mysz','pady','piloty','joysticki','tablety graficzne','monitory','dyski zewnetrzne i przenośne',
        'pendrive','śledzie','kamery internetowe','zestawy i kamery do wideokonferencji','gogle VR','głośniki','mikrofony i słuchawki'}

    context = {
        'categories': categories,
    }

    return HttpResponse(template.render(context, request))

def process(request, price, category):
    #get data from API and machine learning stuff
    rules = create_rules()
    base_price = float(price)
    associated_categories= get_associated_categories(rules, category)

    items_number = 20
    category_number = len(associated_categories)
    items_per_category = items_number // category_number

    cat_id = categories_dict[category]
    items = get_products_from_category(cat_id, num_products=items_per_category, max_price=base_price)
    bundles=[]
    bundles_sample = []
    products = []

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
                        bundles_sample.append(bundle_sample)


    template = loader.get_template('propozycje/zero/productList.html')

    bundles_shuffled = []
    bundles_shuffled = shuffle_bundles(bundles_sample)

    for bundle in bundles_shuffled:
        products = bundle_to_array(bundle)
        bundles.append(products)


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
    """
    bundle = {
        'id': 'abc',
        'products': products
    }

    bundles = []
    bundles.append(bundle)
    """
    context = {
        'bundles': bundles
    }

    return HttpResponse(template.render(context, request))


def buy(request, id):
    #print(id)
    out = []
    ids_split = id.split("a")
    for id_cat in ids_split:
        for name, cat in categories_dict.items():
            if cat == id_cat:
                out.append(name)
    add_new_data(out)
    return HttpResponse('')