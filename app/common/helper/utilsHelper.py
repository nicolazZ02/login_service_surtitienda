import uuid
import hashlib
from fastapi import Request
import base64

class utilsHelper:

    def create_correlation_id(self) -> str:
        return str(uuid.uuid4())
    
    def get_correlation_id(self, request: Request) -> str:
        return request.state.correlation_id
    
    def decrypt_data(self, value:str) -> str:
        try:
            decrypted = base64.b64decode(value).decode('utf-8')
            return decrypted
        except Exception as e:
            print(e)
            return str(e)
        
    def encrypt_data(self, value:str) -> str:
        try:
            encrypted = base64.b64encode(value.encode('utf-8'))
            return encrypted
        except Exception as e:
            print(e)
            return str(e)

    def hash_password(self, password: str) -> str:
        try:
            hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
            return hashed
        except Exception as e:
            print(e)
            return str(e)
        
    def compare_passwords(self, password:str, hashed_password:str)-> bool:
        try:
            val = hashlib.sha256(password.encode('utf-8')).hexdigest() == hashed_password
            print("Entro a validar pass",val)
            return val
        except Exception as e:
            print(e)
            return False
        
    def create_user_token(self)-> str:
        return str(uuid.uuid4().hex)

helper = utilsHelper()