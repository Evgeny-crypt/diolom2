from urllib.parse import urlencode
import requests


APP_ID = 7558099
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
   'client_id': APP_ID,
   'display': 'page',
   'scope': 'status,friends',
   'response_type': 'token',
   'v': '5.122',
}
print('?'.join((AUTH_URL, urlencode(auth_data))))