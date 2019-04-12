import requests
from authorization import token


def get_products_from_category(cat_id, seller_id=None, max_price=None, num_products=None):
    url = "https://api.allegro.pl/offers/listing?category.id="+str(cat_id)
    if seller_id:
        url=url+"&seller.id="+str(seller_id)
    if max_price:
        url=url+'&price.from=0&price.to='+str(max_price)
    if num_products:
        url=url+'&limit='+str(num_products)
    response = requests.get(url, headers={'Accept': 'application/vnd.allegro.public.v1+json',
                                          'content-type': 'application/vnd.allegro.public.v1+json',
                                          'Authorization': 'Bearer ' + token})
    if response.ok:
        return response.json()
    return None


def get_products_from_seller(seller_id, max_price=None, category_id=None, num_products=None):
    url = "https://api.allegro.pl/offers/listing?category.id=" + str(cat_id)
    if category_id:
        url = url + "&category.id=" + str(category_id)
    if max_price:
        url = url + '&price.from=0&price.to=' + str(max_price)
    if num_products:
        url = url + '&limit=' + str(num_products)
    response = requests.get(url, headers={'Accept': 'application/vnd.allegro.public.v1+json',
                                          'content-type': 'application/vnd.allegro.public.v1+json',
                                          'Authorization': 'Bearer ' + token})

    if response.ok:
        return response.json()
    return None






