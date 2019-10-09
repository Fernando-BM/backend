# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Sticker(Base):
    __tablename__ = 'stickers'
    __table_args__ = {'schema': 'proyecto1'}

    idstickers = Column(Integer, primary_key=True)
    precio = Column(Numeric(10, 2), nullable=False)
    url = Column(String(200), nullable=False)
    disponible = Column(Integer, nullable=False)


class Usuario(Base):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': 'proyecto1'}

    correo = Column(String(200), primary_key=True)
    contrasenia = Column(String(500), nullable=False)
