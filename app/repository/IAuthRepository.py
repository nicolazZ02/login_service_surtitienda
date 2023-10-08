# Crear interfaz para el repositorio de reclamaciones
from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session
from app.models import Usuario

class IAuthRepository(ABC):

    @abstractmethod
    def get_user(self, user: Usuario) -> List[Usuario]:
        pass
    @abstractmethod
    def get_rol_by_username(self, username: str) -> List[Usuario]:
        pass
    @abstractmethod
    def recovery_password(self, correo: str) -> List[Usuario]:
        pass
    @abstractmethod
    def confirm_recovery_password(self, user: Usuario) -> List[Usuario]:
        pass