import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote
import xlwings as xw


access_key = os.environ["UPBIT_OPEN_API_ACCESS_KEY"]
secret_key = os.environ["UPBIT_OPEN_API_SECRET_KEY"]
server_url = os.environ["UPBIT_OPEN_API_SERVER_URL"]

payload = {
    "access_key": access_key,
    "nonce": str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = "Bearer {}".format(jwt_token)
headers = {
    "Authorization": authorization,
}

res = requests.get(server_url, headers=headers)
results = res.json()

wb = xw.Book()
ws = wb.sheets[0]


for i, coin in enumerate(results):
    ws.range("A1").offset(i, 0).value = coin["currency"]
    ws.range("B1").offset(i, 0).value = coin["balance"]
