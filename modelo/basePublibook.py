# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Usuario(Base):
    __tablename__ = 'Usuario'
    __table_args__ = {u'schema': 'house'}

    idUsuario = Column(INTEGER(11), primary_key=True)
    nombreUsuario = Column(String(45), nullable=False)
    nombre = Column(String(45), nullable=False)
    apellidoP = Column(String(45), nullable=False)
    apellidoM = Column(String(45))
    contrasenia = Column(String(45), nullable=False)
    correo = Column(String(45), nullable=False)

    VideoJuego = relationship(u'VideoJuego', secondary=u'house.Tener')


class VideoJuego(Base):
    __tablename__ = 'VideoJuego'
    __table_args__ = {u'schema': 'house'}

    idVideoJuego = Column(INTEGER(11), primary_key=True)
    nombre = Column(String(45), nullable=False)
    genero = Column(String(45))
    descripcion = Column(String(45))
    clasificacion = Column(String(45))
    consola = Column(String(45))
    precio = Column(Float(asdecimal=True), nullable=False)


t_Tener = Table(
    'Tener', metadata,
    Column('Usuario_idUsuario', ForeignKey(u'house.Usuario.idUsuario'), primary_key=True, nullable=False, index=True),
    Column('VideoJuego_idVideoJuego', ForeignKey(u'house.VideoJuego.idVideoJuego'), primary_key=True, nullable=False, index=True),
    schema='house'
)
