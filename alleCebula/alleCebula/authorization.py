from alleCebula.credentials import client_id, client_secret, fb_app_id, fb_app_secret, fb_page_id, fb_access_token
from base64 import b64encode
import requests


REDIRECT_URI="http://localhost:5500"


def get_access_token(client_id, client_secret):
    access_token = None
    auth_url = "https://allegro.pl/auth/oauth/token?grant_type=client_credentials"
    s = client_id+':'+client_secret
    s = b64encode(str.encode(s))
    s = str(s)[2:-1]
    response = requests.post(auth_url, headers={'Authorization': 'Basic '+str(s)})
    if response.ok:
        access_token = response.json()['access_token']
    return access_token


def post_to_page(message):
    message = message.replace(' ', '%20')
    message = message.replace('\n', '%0A')
    r = requests.post("https://graph.facebook.com/v3.2/2121524784551397/feed?message="+message+"&access_token="+fb_access_token)

    return r

token = get_access_token(client_id, client_secret)
