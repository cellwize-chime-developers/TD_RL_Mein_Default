from chime.client.naas import NaaSApi
from chime.client.pgw import PGWApi
from chime.client.xpaas import XPaaSApi

NAAS_URL = 'https://<chime-developer-uri>/naas'
XPAAS_URL = 'https://<chime-developer-uri>/xpaas'
PGW_URL = 'https://<chime-developer-uri>/pgw'

naas = NaaSApi(api_root_url=NAAS_URL, timeout=60)
xpaas = XPaaSApi(api_root_url=XPAAS_URL, timeout=60)
pgw = PGWApi(api_root_url=PGW_URL, timeout=60)
