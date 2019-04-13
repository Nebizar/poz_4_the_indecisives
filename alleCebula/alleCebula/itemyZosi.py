import random

from alleCebula.productgetter import get_products_from_category
from propozycje.machineLearning.item_generator import categories_dict

def price_ok(bundle, new_item, max_price):
    result = True
    total_price=float(new_item["sellingMode"]["price"]["amount"])
    for item in bundle:
        total_price+=float(item["sellingMode"]["price"]["amount"])
        if total_price > max_price:
            result=False
            break
    return result

def get_total_price(bundle):
    price=0.0
    #for item in bundle:
    #    price+=float(item["sellingMode"]["price"]["amount"])
    return price


def get_bundles(bundle_base, category, max_price, num_products):
    bundles=[]
    cat_id = categories_dict[category]
    other_items = get_products_from_category(cat_id, max_price=max_price, num_products=num_products)
    for other_item in other_items:
        bundle_sample = bundle_base[:]
        if other_item["sellingMode"]["format"] == "BUY_NOW":
            if get_total_price(bundle_sample)+ float(other_item["sellingMode"]["price"]["amount"]) <= max_price:
                bundle_sample.append(other_item)
                bundles.append(bundle_sample)
    return bundles


def bundle_to_array(bundle):
    id=''
    products=[]
    for item in bundle:
        id+=item["category"]["id"]
        id+="a"
        if(len(item["images"])>0):
            products.append({
                'name':item["name"],
                'price': item["sellingMode"]["price"]["amount"],
                'image':item["images"][0]["url"]
            })
        else:
            products.append({
                'name': item["name"],
                'price': item["sellingMode"]["price"]["amount"],
                'image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAOVBMVEXz9Pa5vsq2u8jN0dnV2N/o6u7w8fTi5OnFydO+ws3f4ee6v8vY2+H29/jy9Pbu7/LJztbCx9HR1ty/NMEIAAAC8ElEQVR4nO3b67ZrMBiFYaSh1HHd/8XuFap1SFolXb7s8T4/18EwOyNCiSIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACryrezAy2kulR+lVl6dqip7Jr412Zyeizj7yjODjYqvhRQTMQm/1rC/OxsvapIht3xehDeN1lIOBSrtt+ZW+t1Kh02GrciEvaDNLl4Ph1e+hqvEk4Z94SZ580WchJGJNyHhH/JlrDR+uC+iU6Yqf7c2JXNga0KTlj/xOP5ujuwdpabML0mz1VXUu7eqtyEP5OAvysdvXerYhMWs4C/a+e9uyg1YXVdXh7sXTtLTagXFcaJ2rlVqQmXgzSOu5f76J5shSasylXC/NVJUbknW6kJLx8lNPNu6WhRaMKPRmmtzB+7WpSasNk+09TjmdPeotSEVbfs0HW7LFXjh2FvUWrC1Z1F1yCt1aRtW4tiE0ZqPk4dp4NUzYaypUW5CaNuGtExjdSLz8HSouCEjRqvnuLcceE/b9D+UQhOGFWZys093e7S2IfoqkFbi5ITRv1NDN24ds7SoKVF4QlfsTa4bjHchOmPI+AiYrgJXQ0uB2qoCWt3g4sWQ034qsF5i4EkbBY3ol43OGsxjIT6luvp7NG+DfhsMYSElc7jpHteAL85BhcthpBQ38zPny1uadD8x3C9JT+habD/RXdfu21rsP822fy5/IR9g/GjxXpjg+ZSKoiEY4OPFrc2GEzCR4O9XL87D4aWcNrgEHFzvkASzhv8UAAJVw3+dwkPNRhAwoMNBpDwYIPiEx5uUHzCww1KT1htX7qEmnD9/SEJSXhutgEJSUjC8/lOKPs+jfla7ajh/qPUhP6Q8C+RcJdKUML7W0HK75vA9+/hrmenM8bHgr/y7pqS8O7a43nEb7x/6Pvo3iddPa3njYx3SKMoO37rwu4mo8LIPJB4fLG2lggZoz3d5l6PQuPWahHTzEgXF79KQQUCAAAAAAAAAAAAAAAAAAAAAAAAAAAAp/gHLTI30QIHnooAAAAASUVORK5CYII='
            })
    bundle = {
        'id': id[:-1],
        'products': products
    }
    return bundle


def shuffle_bundles(bundles):
    random.shuffle(bundles)
    return bundles[:10]

def shuffle_bundles_one(bundles):
    random.shuffle(bundles)
    return [bundles[0]]



def xd(items, associated_categories, items_per_category, max_price):
    bundles=[]
    for item in items:
        if item["sellingMode"]["format"]=="BUY_NOW":
            bundles.append([item])
            other_price = max_price - float(item["sellingMode"]["price"]["amount"])
            for category in associated_categories:
                temp_bundles=[]
                for bundle in bundles:
                    while len(temp_bundles)<3:
                        b=get_bundles(bundle, category, other_price, items_per_category)
                        temp_bundles.append(b)
                bundles.append(temp_bundles)
                print(bundles)
    return bundles









