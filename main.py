import constants
import authenticate
import request

processamento = 'sit_fiscal'
caminho = 'files/Situação Fiscal.pdf'


if __name__ == "__main__":
    authenticate.generate_bearer_token()

    request.generate_data(processamento, caminho, '202301')
