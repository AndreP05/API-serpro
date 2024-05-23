import base64
import json
from requests_pkcs12 import post

from constants import API_SECRETS, URL_AUTH, CERT_FILE, CERT_PASS, append_attributes


def generate_bearer_token():
    credential = base64.b64encode(
        f"{API_SECRETS.get('consumerKey')}:{API_SECRETS.get('consumerSecret')}".encode("utf8")).decode("utf8")
    header = {
        "Authorization": f'Basic {credential}',
        "role-type": "TERCEIROS",
        "content-type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    res = post(URL_AUTH, data=data, headers=header, verify=True, pkcs12_filename=CERT_FILE, pkcs12_password=CERT_PASS)

    dictionary = json.loads(res.content.decode('utf-8').replace("'", '"'))
    append_attributes("accessToken", dictionary.get("access_token"))
    append_attributes("jwtToken", dictionary.get("jwt_token"))
