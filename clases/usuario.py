#! /usr/bin/python2.7

from backend.common.Publicon import obtenerConexion
from backend.modelo.basePublibook import Usuario


def verificaUsuario(correo,password):
	s=obtenerConexion()
	us=s.query(Usuario).filter(Usuario.correo==correo, Usuario.contrasenia==password).first()
	if us!= None:
		usr={"correoUser":us.correo}
		return usr
	else:
		return None

def creaUsuario(dicc):
	s=obtenerConexion()
	usr=Usuario()
	usr.idDepto=dicc['idDepto']
	usr.idRol = dicc['idRol']
	usr.nombre = dicc['nombre']
	usr.a_paterno = dicc['a_paterno']
	usr.a_materno =dicc['a_materno']
	usr.correo = dicc['correo']
	usr.contrasenia = dicc['contrasenia']
	usr.activo=dicc['activo']
	s.add(usr)
	s.commit()
	

def obtenUsuarios():
	s=obtenerConexion()
	users=s.query(Usuario).all()
	usuario={
		"idUsuario" : 0,
		"idDepto" : 0,
		"idRol" : 0,
		"nombre" : 0,
		"a_paterno" : 0,
		"a_materno" : 0,
		"correo" : "",
		"activo" :-1
	}
	lstUser=[]
	for user in users:
		dicc=usuario.copy()
		dicc['idUsuario']=user.idUsuario
		dicc['idDepto']=user.idDepto
		dicc['idRol']=user.idRol
		dicc['nombre']=user.nombre
		dicc['a_paterno']=user.a_paterno
		dicc['a_materno']=user.a_materno
		dicc['correo']=user.correo
		dicc['activo']=user.activo
		lstUser.append(dicc)
	return lstUser

def eliminaUsuarios(id):
	s = obtenerConexion()
	usr = s.query(Usuario).filter(Usuario.idUsuario == id).first()
	usr.activo = 0
	s.commit()



if __name__ == '__main__':
	main()
