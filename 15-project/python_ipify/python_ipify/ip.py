# -*- encoding: utf-8 -*-
import requests


def my_ip():
    req = requests.get('http://members.3322.org/dyndns/getip')
    if req.ok:
        return req.text.strip()
    else:
        raise Exception('network error')
