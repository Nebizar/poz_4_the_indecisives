from credentials import client_id, client_secret
from base64 import b64encode
import requests


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


token = get_access_token(client_id, client_secret)
