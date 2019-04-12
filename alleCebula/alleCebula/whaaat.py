import requests
from authorization import token


def get_items_from_category(cat_id):
    url = "https://api.allegro.pl/offers/listing?category.id="+str(cat_id)
    response = requests.get(url, headers={'Accept': 'application/vnd.allegro.public.v1+json',
                                          'content-type': 'application/vnd.allegro.public.v1+json',
                                          'Authorization': 'Bearer ' + token})
    response = response.json()
    return response






