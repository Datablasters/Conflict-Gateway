# -*- coding: utf-8 -*-

# SQLAlchemy Models for PostGres database on AWS.

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

import settings

DeclarativeBase = declarative_base()

#DB Connect function taking DATABSE settings.py settings
def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

#News Model
class News(DeclarativeBase):
    """Sqlalchemy News model"""
    __tablename__ = "articles_news"
    id = Column(Integer, primary_key=True)
    articletype = Column('articletype', String)
    title = Column('title', String)
    tags = Column('tags', String)
    thumbnail = Column('thumbnail', String)
    tagline = Column('tagline', String)
    website = Column('website', String)
    link = Column('link', String)
    created = Column('created', String)
    hits = Column('hits', Integer)
    user_id = Column('user_id', Integer)

#Jobs Model
class Jobs(DeclarativeBase):
    """Sqlalchemy News model"""
    __tablename__ = "articles_job"
    id = Column(Integer, primary_key=True)
    articletype = Column('articletype', String)
    title = Column('title', String)
    title_slug = Column('title_slug', String)
    created = Column('created', String) 
    author = Column('author', String)
    authorimg = Column('authorimg', String)
    hits = Column('hits', Integer)
    tags = Column('tags', String)
    location = Column('location', String)
    salary = Column('salary', String) 
    thumbnail = Column('thumbnail', String)
    image = Column('image', String)
    tagline = Column('tagline', String)
    body = Column('body', String)
    link = Column('link', String)
    user_id = Column('user_id', Integer) 
    urlsection = Column('urlsection', String)
    
