import requests
from alleCebula.authorization import token
from propozycje.machineLearning.item_generator import get_items_from_api


def get_products_from_category(cat_id, seller_id=None, max_price=None, num_products=None):
    url = "https://api.allegro.pl/offers/listing?category.id={}&sellingMode.format={}".format(str(cat_id), "BUY_NOW")

    if seller_id:
        url = url + "&seller.id=" + str(seller_id)
    if max_price:
        url = url + '&price.from=0&price.to=' + str(max_price)
    if num_products:
        url = url + '&limit=' + str(num_products)
    response = requests.get(url, headers={'Accept': 'application/vnd.allegro.public.v1+json',
                                          'content-type': 'application/vnd.allegro.public.v1+json',
                                          'Authorization': 'Bearer ' + token})
    if response.ok:
        return get_items_from_api(response.json())
    return []
