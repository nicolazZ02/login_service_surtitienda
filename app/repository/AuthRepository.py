# Crear el repositorio implementando la interfaz creada:
from app.repository import IAuthRepository
from app.models import Usuario
from app.common import SessionLocal, UtilsHelper
from typing import List
from datetime import datetime
import re

class AuthRepository(IAuthRepository):
    def __init__(self, db: SessionLocal):
        self.db = db

    def get_rol_by_username(self, username: str):
        try:
            return self.db.query(Usuario).filter(Usuario.username == username).first()
        except Exception as e:
            print(e)
        finally:
            self.db.close()

    def get_user(self, user: Usuario) -> Usuario:
        try:
            user_exist = self.db.query(Usuario).filter(Usuario.username == user.username, Usuario.id_estado == 1, Usuario.intentos_fallidos <= 3).first()
            if user_exist is not None:
                # user_exist.ultima_conexion = datetime.now()
                user_exist.intentos_fallidos = user_exist.intentos_fallidos + 1
                self.db.commit()
                valid_password = UtilsHelper.compare_passwords(user.clave, user_exist.clave)
                if valid_password:
                    user_exist.intentos_fallidos = 0
                    self.db.commit()
                    return user_exist
                else:
                    return None
        except Exception as e:
            print(e)
            return None


    # def log_to_database(self):
    #     try:
    #         with open('Logs/app.log', 'r') as file:
    #             for line in file:
    #                 regex = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - .* - \/.*\/(.*) - (.*) - end in time \(ms\): ([0-9.]+) - correlationId ([a-f0-9-]+) - Response: (.*)'
    #                 match = re.search(regex, line)
    #                 if match:
    #                     fecha = match.group(1)
    #                     endpoint = match.group(2)
    #                     metodo = match.group(3)
    #                     tiempo_ms = match.group(4)  # Asignar como cadena de texto
    #                     correlation_id = match.group(5)
    #                     response = match.group(6)
                        
    #                     log = Log(
    #                         fecha=fecha,
    #                         endpoint=endpoint,
    #                         metodo=metodo,
    #                         tiempo_ms=tiempo_ms,  # Mantener como cadena de texto
    #                         correlation_id=correlation_id,
    #                         response=response
    #                     )
    #                     self.db.add(log)
    #         self.db.commit()
    #         self.db.refresh(log)
    #     except Exception as e:
    #         # Manejar la excepción adecuadamente
    #         print(e)
    #         return e
    #     finally:
    #         self.db.close()

    def recovery_password(self, correo: str, token: str) -> Usuario:
        try:
            user = self.db.query(Usuario).filter(Usuario.correo == correo).first()
            if user is None:
                return None
            else:
                user.token = token
                user.updated_at = datetime.now()
                self.db.commit()
                self.db.refresh(user)
                return user
        except Exception:
            # Raise exception
            return None
        finally:
            self.db.close()
    
    def confirm_recovery_password(self,token: str, id: int, password:str):
        try:
            user=self.db.query(Usuario).filter(Usuario.id_usuario == id).first()
            if user.token == token:
                user.password = UtilsHelper.hash_password(password)
                user.token = None
                user.update_at = datetime.now()
                self.db.commit()
                self.db.refresh()
            elif user.token != None or user.token != token:
                user = None
            return user
        except Exception as e:
            return None
        finally:
            self.db.close()