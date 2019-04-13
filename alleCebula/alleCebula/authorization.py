from alleCebula.credentials import client_id, client_secret, fb_app_id, fb_app_secret, fb_page_id, fb_access_token
from base64 import b64encode
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import webbrowser
import facebook

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
"""

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


def login_to_facebook(url):
    graph = facebook.GraphAPI(access_token=fb_access_token)
    redirect_uri = REDIRECT_URI
    perms = ["manage_pages", "publish_pages"]
    fb_login_url = graph.get_auth_url(fb_app_id, redirect_uri, perms)
    print(fb_login_url)
    return
"""

"""
def get_fb_auth(fb_access_token):
    graph = facebook.GraphAPI(access_token=fb_access_token)
    pages_data = graph.get_object("/me/accounts")

    page_id = fb_page_id
    page_token = None

    for item in pages_data['data']:
        if item['id'] == page_id:
            page_token = item['access_token']

    return page_token
"""

def post_to_page(message):
    message = message.replace(' ', '%20')
    message = message.replace('\n', '%0A')
    r = requests.post("https://graph.facebook.com/v3.2/2121524784551397/feed?message="+message+"&access_token="+fb_access_token)

    print('----------------------')
    print(r)
    print('----------------------')
    #graph = facebook.GraphAPI(access_token=fb_access_token)
    #status = graph.put_wall_post(message)
    #status=graph.put_object(parent_object='2121524784551397', connection_name="feed", message=message)
    return r

token = get_access_token(client_id, client_secret)
#page_token=get_fb_auth(fb_access_token)
#user_code = authorize_user(client_id)