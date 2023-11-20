from chime.client.naas import NaaSApi
from chime.client.pgw import PGWApi
from chime.client.xpaas import XPaaSApi
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from utils.context import context
import os

# Configure CHIME Services endpoints
NAAS_URL = 'https://naas.chime-prod.gcp.de.pri.o2.com/naas'
XPAAS_URL = 'https://xpaas.chime-prod.gcp.de.pri.o2.com/xpaas'
PGW_URL = 'https://pgw.chime-prod.gcp.de.pri.o2.com/pgw'
AUTH_URL = 'https://am.chime-prod.gcp.de.pri.o2.com/gateway/chime/oauth/token'

# Configure Client_Id and Client_Secret to enable authentication
CLIENT_ID = context.get('CLIENT_ID')
CLIENT_SECRET = context.get('CLIENT_SECRET')

HEADERS = {}
CERT_PATH = os.path.dirname(__file__) + '/STRootCA-SSLSubCA.pem'
# CHIME uses Oauth2 client credentials authentication flow
if CLIENT_ID is not None and CLIENT_SECRET is not None:
    client = BackendApplicationClient(client_id=CLIENT_ID)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=AUTH_URL, client_id=CLIENT_ID,
                              client_secret=CLIENT_SECRET, verify=CERT_PATH)

    # init API client headers with access_token
    HEADERS = {'Authorization': 'Bearer ' + token.get('access_token')}

# Init  clients
naas = NaaSApi(api_root_url=NAAS_URL, timeout=60, headers=HEADERS, ssl_verify=CERT_PATH)
xpaas = XPaaSApi(api_root_url=XPAAS_URL, timeout=60, headers=HEADERS, ssl_verify=CERT_PATH)
pgw = PGWApi(api_root_url=PGW_URL, timeout=60, headers=HEADERS, ssl_verify=CERT_PATH)
