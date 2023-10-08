# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    id_tipo = Column(Integer)
    nombre = Column(String(100))
    apellido = Column(String(100))
    n_docu = Column(String(13))
    username = Column(String(100))
    correo = Column(String(100))
    clave = Column(String(700))
    id_estado = Column(Integer)
    intentos_fallidos = Column(Integer)

    @classmethod
    def from_request_create(cls, request):
        return cls(
            nombre = request.nombre,
            apellido = request.apellido,
            n_docu = request.n_docu,
            username = request.username,
            correo = request.correo,
            clave = request.clave,
            id_estado = request.id_estado,
            id_tipo = request.id_tipo
        )
    

    @classmethod
    def from_request_update(cls, request):
        return cls(
            nombre = request.nombre,
            apellido = request.apellido,
            n_docu = request.n_docu,
            username = request.username,
            correo = request.correo,
            clave = request.clave,
            id_estado = request.id_estado,
            id_tipo = request.id_tipo
        )
    

    def serialize(self):
        return {
            'id_usuario' : self.id_usuario,
            'id_tipo' : self.id_tipo,
            'nombre' : self.nombre,
            'apellido' : self.apellido,
            'n_docu' : self.n_docu,
            'username' : self.username,
            'correo' : self.correo,
            'clave' : self.clave,
            'id_estado' : self.id_estado,
        }