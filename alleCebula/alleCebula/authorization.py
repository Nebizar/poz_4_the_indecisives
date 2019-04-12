from credentials import client_id, client_secret
from base64 import b64encode
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import webbrowser

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


def authorize_user(client_id, redirect_uri = REDIRECT_URI):

    class Handler(BaseHTTPRequestHandler):
        def __init__(self, request, address, server):
            super().__init__(request, address, server)

        def do_GET(self):
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.server.path = self.path
            self.server.code = self.path.rsplit('?code=', 1)[-1]

    auth_url="https://allegro.pl/auth/oauth/authorize" \
             "?response_type=code&client_id={}&redirect_url={}"\
        .format(client_id, redirect_uri)

    webbrowser.open(auth_url)

    redirect_uri = requests.utils.urlparse(redirect_uri)
    httpd = HTTPServer((redirect_uri.hostname, redirect_uri.port), Handler)
    httpd.handle_request()
    httpd.server_close()
    return httpd.code


token = get_access_token(client_id, client_secret)
#user_code = authorize_user(client_id)