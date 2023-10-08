from pydantic import BaseModel, Field

email_example = "example@example.com"
    
class LoginRequest(BaseModel):
    username: str = Field(..., example="Pepito.perez02")
    clave: str = Field(..., example="123435678")

class UserPasswordRequest(BaseModel):
    password: str = Field(..., example="123456789")

class UserRecoveryPasswordRequest(BaseModel):
    correo: str = Field(..., example=email_example)