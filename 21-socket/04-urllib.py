import urllib.request
import json


def stock_price(code):
    url = 'https://financialmodelingprep.com/api/company/price/' + code
    req = urllib.request.Request(url=url)
    with urllib.request.urlopen(req) as f:
        body = f.read().decode('utf-8')
        body = body.replace('<pre>', '').replace('</pre>', '')
        data = json.loads(body)
    return data


if __name__ == '__main__':
    print(stock_price('AAPL'))

