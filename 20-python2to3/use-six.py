from __future__ import print_function

import json
import sys
from contextlib import closing

from six.moves import map
from six.moves.urllib_request import urlopen, Request


def stock_price(code):
    url = 'https://financialmodelingprep.com/api/company/price/' + code
    req = Request(url=url)
    with closing(urlopen(req)) as f:
        body = f.read().decode('utf-8')
        body = body.replace('<pre>', '').replace('</pre>', '')
        data = json.loads(body)
    return data


if __name__ == '__main__':
    print('running with Python', sys.version)
    print(map(stock_price, ['AAPL', 'GOOGL']))
    print(list(map(stock_price, ['AAPL', 'GOOGL'])))
