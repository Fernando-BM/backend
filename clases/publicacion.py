import sys
sys.path.append('..')
from common.Publicon import obtenerConexion
from modelo.basePublibook import Publicacion
#from common.Publicon import obtenerConexion
#from modelo.basePublibook import Publicacion


def creaPublicacion(dicc):
    s = obtenerConexion()
    publicacion = Publicacion()
    publicacion.autorP = dicc['autorP']
    publicacion.ISBN = dicc['ISBN']
    publicacion.apoyo = dicc['apoyo']
    publicacion.idTipo = dicc['idTipo']
    publicacion.idSolicitud = dicc['idSolicitud']
    publicacion.nombre = dicc['nombre']
    publicacion.Cat_tipo_idTipo=1 
    s.add(publicacion)
    s.commit()
    print(publicacion.nombre)

def muestraPublicaciones():
    s = obtenerConexion()
    publicaciones = s.query(Publicacion).all()
    return publicaciones

def muestraPublicacion(nombre):
    s = obtenerConexion()
    publicacion = s.query(Publicacion).filter(Publicacion.nombre == nombre).first()
    return publicacion

def eliminaPublicacion(nombre):
    s = obtenerConexion()
    publicacion = s.query(Publicacion).filter(Publicacion.nombre == nombre).first()
    publicacion.activo = 0
    s.commit()

registro = {'autorP': 'Ailyn Rebollar', 'ISBN':'128595409-3', 'apoyo' : 'CONACYT', 'idTipo': 1, 
'idSolicitud' : 9, 'nombre': 'Publicacion 1', 'idPublicacion' : 1}
creaPublicacion(registro)