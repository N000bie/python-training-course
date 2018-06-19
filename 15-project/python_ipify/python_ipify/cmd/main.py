# -*- encoding: utf-8 -*-
from ..ip import my_ip


def main():
    try:
        print('your external IP is:', my_ip())
    except:
        print('network error')
