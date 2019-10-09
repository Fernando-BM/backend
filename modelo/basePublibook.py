# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cargo(Base):
    __tablename__ = 'Cargo'
    __table_args__ = {'schema': 'publibook2.0'}

    idCargo = Column(INTEGER(11), primary_key=True)
    descripcionCar = Column(String(45))


class Encargado(Cargo):
    __tablename__ = 'Encargado'
    __table_args__ = {'schema': 'publibook2.0'}

    idEncargado = Column(ForeignKey('publibook2.0.Cargo.idCargo', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    descripcionEn = Column(String(45))
    nombre_primero = Column(String(45))
    nombre_segundo = Column(String(45))
    apellido_primero = Column(String(45))
    apellido_segundo = Column(String(45))


class CatDepto(Base):
    __tablename__ = 'Cat_depto'
    __table_args__ = {'schema': 'publibook2.0'}

    idDepto = Column(INTEGER(11), primary_key=True)
    descripcion = Column(String(45), nullable=False)


class CatTipo(Base):
    __tablename__ = 'Cat_tipo'
    __table_args__ = {'schema': 'publibook2.0'}

    idTipo = Column(INTEGER(11), primary_key=True)
    descripcion = Column(String(45), nullable=False)


class EstadoPublicacion(Base):
    __tablename__ = 'Estado_publicacion'
    __table_args__ = {'schema': 'publibook2.0'}

    idEstado = Column(INTEGER(11), primary_key=True)
    descripcion = Column(String(45))


class SolicitudPublicacion(Base):
    __tablename__ = 'Solicitud_publicacion'
    __table_args__ = {'schema': 'publibook2.0'}

    idSolicitud = Column(INTEGER(11), primary_key=True)
    nombre_publicacion = Column(String(200), nullable=False)
    justificacion = Column(String(450))
    docencia = Column(TINYINT(1))
    investigacion = Column(TINYINT(1))
    difusion = Column(TINYINT(1))
    publico = Column(String(45))
    mercado = Column(INTEGER(11))
    ejemplares = Column(INTEGER(11))
    fecha = Column(DateTime)
    autorSol = Column(String(45))
    editor = Column(String(45))
    correo_autor = Column(String(45))
    correo_editor = Column(String(45))
    tel_autor = Column(String(15))
    tel_editor = Column(String(15))


class Publicacion(Base):
    __tablename__ = 'Publicacion'
    __table_args__ = {'schema': 'publibook2.0'}

    idPublicacion = Column(INTEGER(11), primary_key=True)
    autorP = Column(String(45), nullable=False)
    ISBN = Column(String(25), nullable=False)
    apoyo = Column(String(45), server_default=text("'NINGUNO'"))
    idSolicitud = Column(ForeignKey('publibook2.0.Solicitud_publicacion.idSolicitud', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    nombre = Column(String(200), nullable=False)
    activo = Column(INTEGER(11), nullable=False, server_default=text("'1'"))
    Cat_tipo_idTipo = Column(ForeignKey('publibook2.0.Cat_tipo.idTipo'), nullable=False, index=True)

    Cat_tipo = relationship('CatTipo')
    Solicitud_publicacion = relationship('SolicitudPublicacion')


class Usuario(Base):
    __tablename__ = 'Usuario'
    __table_args__ = {'schema': 'publibook2.0'}

    idUsuario = Column(INTEGER(11), primary_key=True)
    idDepto = Column(ForeignKey('publibook2.0.Cat_depto.idDepto'), nullable=False, index=True)
    idRol = Column(INTEGER(11), nullable=False)
    nombre = Column(String(45), nullable=False)
    a_paterno = Column(String(45), nullable=False)
    a_materno = Column(String(45), nullable=False)
    correo = Column(String(45), nullable=False)
    contrasenia = Column(String(450), nullable=False)
    activo = Column(INTEGER(11), nullable=False, server_default=text("'1'"))

    Cat_depto = relationship('CatDepto')


class Bitacora(Base):
    __tablename__ = 'Bitacora'
    __table_args__ = {'schema': 'publibook2.0'}

    idBitacora = Column(INTEGER(11), primary_key=True)
    idEstado = Column(ForeignKey('publibook2.0.Estado_publicacion.idEstado', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    idUsuario = Column(ForeignKey('publibook2.0.Usuario.idUsuario', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    IdPublicacion = Column(ForeignKey('publibook2.0.Publicacion.idPublicacion', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    idEncargado = Column(ForeignKey('publibook2.0.Encargado.idEncargado', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    concluido = Column(TINYINT(1))
    fecha = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

    Publicacion = relationship('Publicacion')
    Encargado = relationship('Encargado')
    Estado_publicacion = relationship('EstadoPublicacion')
    Usuario = relationship('Usuario')
