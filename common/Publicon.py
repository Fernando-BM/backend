#!/usr/bin/python
# -*- coding: utf8 -*-

from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os

def obtenerConexion():
    host = 'localhost'
    user = 'admin'
    database = 'publibook2.0'
    password = 'Goy@goy@123!' 
    # create an engine
    connection = 'mysql+pymysql://'+user+':'+password+'@'+host+':3306/'+database
    engine = sqlalchemy.create_engine(connection)
    connection = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


