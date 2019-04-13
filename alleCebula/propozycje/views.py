from django.shortcuts import render
from propozycje.machineLearning.rules import create_rules, get_associated_categories, add_new_data
from alleCebula.productgetter import get_products_from_category, get_products_from_seller
from propozycje.machineLearning.item_generator import categories_dict
from alleCebula.itemyZosi import bundle_to_array, shuffle_bundles, shuffle_bundles_one, get_total_price
from django.http import HttpResponse
from django.template import loader

def propositions(request):
    template = loader.get_template('propozycje/zero/index.html')
    #TODO zamienic na wlasciwe kategorie
    categories = {'myszki','klawiatury','zestaw klawiatura i mysz','pady','piloty','joysticki','tablety graficzne','monitory','dyski zewnetrzne i przenosne',
        'pendrive','sledzie','kamery internetowe','zestawy i kamery do wideokonferencji','gogle VR','glosniki','mikrofony i sluchawki'}

    context = {
        'categories': categories,
    }

    return HttpResponse(template.render(context, request))

def compute(price, category):
    #get data from API and machine learning stuff
    rules = create_rules()
    base_price = float(price)
    associated_categories= get_associated_categories(rules, category)

    items_number = 10
    category_number = len(associated_categories)
    items_per_category = items_number // category_number

    cat_id = categories_dict[category]
    items = get_products_from_category(cat_id, num_products=items_per_category, max_price=base_price)
    bundles = []
    products = []
    bundles = []
    category_items=[]

    #bundles_sample = xd(items, associated_categories, items_per_category, base_price)

    for category in associated_categories:
        cat_id = categories_dict[category]
        c_items= get_products_from_category(cat_id, max_price=base_price, num_products=items_per_category)
        category_items.append(c_items)



    for item in items:
        if item["sellingMode"]["format"] == "BUY_NOW":
            for category in category_items:
                other_items=category
                j = 0
                for other_item in other_items:
                    bundle_sample = []
                    bundle_sample.append(item)
                    j += 1
                    if j > 3:
                        break
                    if other_item["sellingMode"]["format"] == "BUY_NOW":
                        bundle_sample.append(other_item)
                        bundles.append(bundle_sample)
                        for new_category in category_items:
                            another_items = new_category
                            i = 0
                            for another_item in another_items:
                                i += 1
                                if i > 3:
                                    break
                                another_bundle_sample = [item, other_item]
                                if another_item["sellingMode"]["format"] == "BUY_NOW":
                                    another_bundle_sample.append(another_item)
                                    bundles.append(another_bundle_sample)

    return bundles

def process(request, price, category):
    bundles_sample = []
    bundles = []

    bundles_sample = compute(price, category)

    template = loader.get_template('propozycje/zero/productList.html')

    bundles_shuffled = []
    bundles_shuffled = shuffle_bundles(bundles_sample)

    for bundle in bundles_shuffled:
        products = bundle_to_array(bundle)
        bundles.append(products)

    context = {
        'bundles': bundles
    }

    return HttpResponse(template.render(context, request))

def process_one(request, price, category):
    bundles_sample = []
    bundles = []

    bundles_sample = compute(price, category)

    template = loader.get_template('propozycje/zero/productList.html')

    bundles_shuffled = []
    bundles_shuffled = shuffle_bundles_one(bundles_sample)

    for bundle in bundles_shuffled:
        products = bundle_to_array(bundle)
        bundles.append(products)

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