# -*- encoding: utf-8 -*-
import logging
import sys


def enable_sql_log():
    logging.basicConfig(handlers=[
        logging.StreamHandler(sys.stdout)
    ])
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
