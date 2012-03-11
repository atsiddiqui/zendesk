import urllib
import requests
import simplejson as json
from url_mapping import API_URL_MAPPING

from django.conf import settings

AUTH_USERNAME = 'tauquir.ali@gmail.com'
AUTH_PASSWORD = 'Tauquir@1'
API_BASE_URL = 'https://launchyad.zendesk.com'

class ZenLib(object):

    def __init__(self, ):
        self.base_url = API_BASE_URL
        self.headers = {'Content-type': 'application/json',
                        'Accept': 'text/plain',
                        }

    def _construct_url(self, url_map_key):
        return '%s%s' % (self.base_url, API_URL_MAPPING[url_map_key])

    def _make_request(self, url_map_key, data={}, extra_param=None, method='GET'):
        if method == 'GET':
            if data:
                url = '%s?%s' % (self._construct_url(url_map_key), urllib.urlencode(data))
            else:
                url = self._construct_url(url_map_key)
            if extra_param:
                url = url % (extra_param)
            response = requests.get(url, auth=(AUTH_USERNAME, AUTH_PASSWORD))

        elif method == 'POST':
            pass
        elif method == 'PUT':
            pass
        elif method == 'DELETE':
            pass
        return json.loads(response.content)
