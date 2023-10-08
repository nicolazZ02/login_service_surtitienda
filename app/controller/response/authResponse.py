from typing import Any,Optional, TypeVar,Type
from pydantic import BaseModel
from app.common import settings
from dataclasses import dataclass

Model = TypeVar('Model', bound=BaseModel)

@dataclass
class TokenResponses():
    access_token: str = settings.ACCESS_TOKEN
    token: str = Optional[None]
    username: str = Optional[None]
    
    def __init__(self, token: str, username: str):
        self.token = token
        self.username = username

    @classmethod
    def from_response_token(cls, response):
        return cls(
            token = response.token,
            username = response.username,
        )
        
    def serialize(self):
        return {
            'access_token': self.access_token,
            'token': self.token,
            'username': self.username,
        }

class UsersReponse(BaseModel):
    id_usuario: int
    id_tipo: int
    n_docu: str
    nombre: str
    apellido: str
    id_estado: int
    username: str
    correo: str
    intentos_fallidos: Optional[int]

    @classmethod
    def from_orm(cls: Type[Model], obj: Any) -> Model:
        return super().from_orm(obj)
    
    def __init__(self, n_docu: str, nombre: str, id_tipo: int,apellido: str,username: str,correo: str,id_estado: int, id_usuario: int, cargo:str, photo:str, intentos_fallidos:int):
        self.id_usuario = id_usuario
        self.n_docu = n_docu
        self.id_tipo = id_tipo
        self.nombre = nombre
        self.apellido = apellido
        self.username = username
        self.correo = correo
        self.id_estado = id_estado
        self.intentos_fallidos = intentos_fallidos
        
    class Config:
        orm_mode = True