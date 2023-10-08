# Crear interfaz para el servicio de reclamaciones
from abc import ABC, abstractmethod
from typing import List
from app.controller.response.authResponse import TokenResponses
from app.controller.response.authResponse import UsersReponse
from app.controller.request.authRequest import LoginRequest

class IAuthService(ABC):

    @abstractmethod
    def login_user(self, login: LoginRequest) -> list[TokenResponses]:
        pass
    @abstractmethod
    def get_rol_by_username(self, username: str) -> list[UsersReponse]:
        pass

    @abstractmethod
    def recovery_password(self, correo: str) -> list[UsersReponse]:
        pass
    @abstractmethod
    def confirm_recovery_password(self, id: int, token: str, password: str ) -> List[UsersReponse]:
        pass