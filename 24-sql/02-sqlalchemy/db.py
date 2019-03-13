# -*- encoding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import sqlalchemy_url

Base = declarative_base()

_cached_engine = None
_cached_session = None


def get_engine():
    global _cached_engine
    if _cached_engine is None:
        _cached_engine = create_engine(sqlalchemy_url)

    return _cached_engine


def get_session():
    global _cached_session
    if _cached_session is None:
        _cached_session = sessionmaker(bind=get_engine())
    return _cached_session()
