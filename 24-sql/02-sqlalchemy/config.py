# -*- encoding: utf-8 -*-
import urllib.parse

params = urllib.parse.quote_plus(
    'DRIVER={SQL Server};'
    'SERVER=192.168.32.139;'
    'DATABASE=TestDB;'
    'UID=sa;'
    'PWD=atc.1234'
)

sqlalchemy_url = 'mssql+pyodbc:///?odbc_connect=' + params
