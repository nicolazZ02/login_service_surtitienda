from typing import Any,Dict,Optional
from pydantic import AnyHttpUrl,BaseSettings
from .utilsHelper import helper as UtilsHelper
import os
import json
from dotenv import load_dotenv

load_dotenv()

class ConstantsHelper(BaseSettings):
    API_V1_STR: str = "/api/v1/auth"
    DOCS_URL: str = "/docs"

    SECRET_KEY: str = UtilsHelper.decrypt_data(os.getenv("SECRET_KEY"))

    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = None
    ACCESS_TOKEN: str = "x-access-token"
    SERVER_NAME: Optional[str] = None
    SERVER_HOST: AnyHttpUrl = None

    CLIENT_URL: str = os.getenv("CLIENT_URL")
    CLIENT_CONFIRM_RECOVERY_PASSWORD_ROUTE = "/users/recovery-password/confirm/"


    BACKEND_CORS_ORIGINS: list = json.loads(os.getenv("BACKEND_CORS_ORIGINS"))

    PROJECT_NAME: str = "Servicio del Login"
    DESCRIPTION_APP: str = "API del microservicio del login"
    VERSION_APP: str = "1.0.0"

    #SMTP
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = os.getenv("SMTP_PORT")
    SMTP_HOST: Optional[str] = os.getenv("SMTP_HOST")
    SMTP_USER: Optional[str] = os.getenv("SMTP_USER")
    SMTP_PASSWORD: Optional[str] = os.getenv("SMTP_PASSWORD")
    SMTP_FROM_EMAIL: Optional[str] = os.getenv("SMTP_FROM_EMAIL")
    SMTP_FROM_NAME: Optional[str] = os.getenv("SMTP_FROM_NAME")
    EMAILS_FROM_EMAIL: Optional[str] = os.getenv("EMAILS_FROM_EMAIL")

    GET_STATIC_ROUTE: str = "/static"

    #ROUTES
    LOGIN_ROUTE: str = "/login"
    GET_ROL_BY_USERNAME_ROUTE: str = "/login/username/{username:str}"
    POST_RECOVERY_PASSWORD_ROUTE: str = "/login/recovery_password"
    PUT_CONFIRM_RECOVERY_PASSWORD_ROUTE: str = "/login/recovery_password/{id:int}/{token:str}"
    PUT_ATTEMPS_FAIL_ROUTE: str = "/login/{username:str}"

    #MESSAGES
    LOGIN_USER_NOT_FOUND = "El usuario no se encontro"
    LOGIN_USER_SUCCESS = "El usuario se encontro correctamente"
    ATTEMPS_NOT_FOUND = "No hay intentos"
    ATTEMPS_SUCCESS = "Se intento correctamente"
    GET_ROL_BY_ID_SUCCESS = "El rol se encontro correctamente"
    RECOVERY_PASSWORD_NOT_FOUND = "Este correo no existe"
    RECOVERY_PASSWORD_BAD_REQUEST = "No se encuentra este correo"
    RECOVERY_PASSWORD_SUCCESS = "Correo enviado"

    # Header Midleware
    CORRELATION_ID_HEADER: str = "X-Correlation-id"

    #Logs Settings
    LEVEL_LOG: str = "INFO"
    FILENAME_LOG: str = "app.log"
    DATEFORMAT_LOG: str = "%Y-%m-%d %H:%M:%S"
    FORMAT_LOG: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # JWT
    HTTP_JWT = "PRUEBAS"
    ISS_JWT = "JWTAuthenticationServer"
    AUD_JWT = "JWTServicePostmanClient"
    EXP_JWT = 120
    DECODE_JWT = "utf-8"


    # HTTP STATUS
    HTTP_400_BAD_REQUEST: Dict[str, Any] = {
        "status_code": 400,
        "description": "Bad Request"
    }
    HTTP_404_NOT_FOUND: Dict[str, Any] = {
        "status_code": 404,
        "description": "Not Found"
    }
    HTTP_500_INTERNAL_SERVER_ERROR: Dict[str, Any] = {
        "status_code": 500,
        "description": "Internal Server Error"
    }

    class Config:
        case_sensitive = True

settings = ConstantsHelper()