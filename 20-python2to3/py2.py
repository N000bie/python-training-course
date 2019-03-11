#!/usr/bin/env python2
""" try
    python -m lib2to3 py2.py
to check python 3 version
"""
import sys

from urllib2 import Request, urlopen
import json


def stock_price(code):
    url = 'https://financialmodelingprep.com/api/company/price/' + code
    req = Request(url=url)
    f = urlopen(req)
    try:
        body = f.read().decode('utf-8')
        body = body.replace('<pre>', '').replace('</pre>', '')
        data = json.loads(body)
    finally:
        f.close()
    return data


if __name__ == '__main__':
    print 'running with Python', sys.version
    print map(stock_price, ['AAPL', 'GOOGL'])
