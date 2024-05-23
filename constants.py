import os
import json

with open('files/keys.json') as keys:
    secrets = keys.read()

URL_AUTH = "https://autenticacao.sapi.serpro.gov.br/authenticate"
URL_REQUEST = "https://gateway.apiserpro.serpro.gov.br/integra-contador/v1/Consultar"
URL_TRANSMIT = "https://gateway.apiserpro.serpro.gov.br/integra-contador/v1/Emitir"
URL_SUPPORT = "https://gateway.apiserpro.serpro.gov.br/integra-contador/v1/Apoiar"
CERT_FILE = f"{os.path.dirname(os.path.realpath(__file__))}\\files\\certificado.pfx"
CERT_PASS = ''
API_SECRETS = json.loads(secrets)

ACCOUNTANT_CODE = ''
WARRANT_CODE = ''
CLIENT_CODE = ''


def append_attributes(key, value):
    with open('files/keys.json') as f:
        data = json.load(f)
    data.update({key: value})
    with open('files/keys.json', 'w') as f:
        json.dump(data, f)


def read_keys():
    global API_SECRETS

    with open('files/keys.json') as chaves:
        sec = chaves.read()
    API_SECRETS = json.loads(sec)
    return API_SECRETS
