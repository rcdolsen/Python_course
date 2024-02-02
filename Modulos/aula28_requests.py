# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs

import requests

# http:// -> padrao porta 80
# https:// -> padrao porta 443
url = 'http://localhost:3004/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.json)
print(response.text)
