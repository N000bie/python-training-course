import requests
import json


def stock_price(code):
    url = 'https://financialmodelingprep.com/api/company/price/' + code
    r = requests.get(url)
    body = r.text
    data = r.text.replace('<pre>', '').replace('</pre>', '')
    return json.loads(data)


if __name__ == '__main__':
    print(stock_price('AAPL'))

