from productgetter import get_products_from_seller
from propozycje.machineLearning.item_generator import categories_dict

def get_total_price(bundle):
    price=0.0
    for item in bundle:
        price+=float(item["sellingMode"]["price"]["amount"])
    return price


def get_bundles(bundles, seller_id, category_id, max_price, num_products):
    new_bundles=[]
    new_items=get_products_from_seller(seller_id, cat_id=category_id, max_price=max_price, num_products=num_products)
    for item in new_items:
        if item["sellingMode"]["format"] == "BUY_NOW":
            price=float(item["sellingMode"]["price"]["amount"])
            for bundle in bundles:
                if get_total_price(bundle)+price<=max_price:
                    bundle.append(item)
                    new_bundles.append(bundle)
    return new_bundles


def process_xd(items, categories, max_price, num_products):
    for item in items:
        if item["sellingMode"]["format"] == "BUY_NOW":
            seller_id=item["seller"]["id"]
            bundles=[[item]]
            for category in categories:
                cat_id = categories_dict[category]
                bundles=get_bundles(bundles, seller_id, category, max_price, num_products)
    return bundles


def bundle_to_array(bundle):
    products=[]
    for item in bundle:
        products.append({
            'name':item["name"],
            'price': item["sellingMode"]["price"]["amount"],
            'image':item["images"][0]["url"]
        })
    return products

