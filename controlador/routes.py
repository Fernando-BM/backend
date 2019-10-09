#! /usr/bin/python2.7
#from backEnd.common.Publicon import obtenerConexion
from backend.clases.usuario import verificaUsuario,creaUsuario,obtenUsuarios
from flask import Flask, request,jsonify,make_response
app = Flask(__name__)


@app.route('/ruta')
def get_path():
	#sys.path.append("..")
	return "holis"

@app.route("/login",methods=['GET', 'POST'])
def login():
	data=request.json
	correo=data['username']
	password=data['password']
	usr=verificaUsuario(correo,password)
	if usr!=None:
		return make_response(jsonify(usr), 200)
	else:
		return make_response(jsonify(message="no conectado"), 220)

@app.route("/admin/creaRepresentante",methods=['GET', 'POST'])
def creaRepresentante():
	data=request.json
	dicc={}
	dicc['idDepto']=data['idDepto']
	dicc['idRol']=2
	dicc['nombre']=data['nombre']
	dicc['a_paterno']=data['a_paterno']
	dicc['a_materno']=data['a_materno']
	dicc['correo']=data['correo']
	dicc['contrasenia']=data['password']
	dicc['activo']=1
	creaUsuario(dicc)
	return make_response(jsonify(message="agregado"), 200)

@app.route("/admin/creaAutor",methods=['GET', 'POST'])
def creaAutor():
	data=request.json
	dicc={}
	dicc['idDepto']=-1
	dicc['idRol']=3
	dicc['nombre']=data['nombre']
	dicc['a_paterno']=data['a_paterno']
	dicc['a_materno']=data['a_materno']
	dicc['correo']=data['correo']
	dicc['contrasenia']=data['password']
	dicc['activo']=1
	creaUsuario(dicc)
	return make_response(jsonify(message="agregado"), 200)

@app.route("/admin/obtenUsr")
def obtenUsr():
	listaUsuarios=obtenUsuarios()
	if listaUsuarios:
		return make_response(jsonify(listaUsuarios), 200)
	else:
		return make_response(jsonify(message="Sin usuarios"), 220)


if __name__ == "__main__":
	app.run()
