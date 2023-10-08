from sqlalchemy.orm import Session
from pydantic import EmailStr
from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.repository.AuthRepository import AuthRepository
from app.service import IAuthService
from app.controller.response.authResponse import UsersReponse
from app.controller.response.authResponse import TokenResponses
from app.controller.request.authRequest import LoginRequest
from app.common import BaseResponseDTO, StatusCodes, settings, SessionLocal, Errors, UtilsHelper, send_mail

templates = Jinja2Templates(directory="app/common/templates")

class AuthService(IAuthService):
    def __init__(self, db: SessionLocal):
        self.db = db
        self.repository = AuthRepository(db)

    def get_rol_by_username(self, username:str) -> list[UsersReponse]:
        try:
            usuario = self.repository.get_rol_by_username(username)
            if usuario is None:
                return [BaseResponseDTO(
                    code=StatusCodes.NOT_FOUND.value,
                    status=StatusCodes.NOT_FOUND.name,
                    message=settings.LOGIN_USER_NOT_FOUND,
                    idTransaction="",
                    data=[]
                )]
            else:
                return [BaseResponseDTO(
                    code=StatusCodes.OK.value,
                    status=StatusCodes.OK.name,
                    message=settings.GET_ROL_BY_ID_SUCCESS,
                    idTransaction="",
                    data=[UsersReponse.from_orm(usuario)]
                )]
        except Exception as e:
            return [BaseResponseDTO(
                code=StatusCodes.INTERNAL_SERVER_ERROR.value,
                status=StatusCodes.INTERNAL_SERVER_ERROR.name,
                message=str(e),
                idTransaction="",
                data= [Errors.HTTP_500_INTERNAL_SERVER_ERROR]
            )]

    def login_user(self, login: LoginRequest) -> list[TokenResponses]:
        try:
            user = self.repository.get_user(login)
            if user is None:
                return BaseResponseDTO(
                    code=StatusCodes.NOT_FOUND.value,
                    status=StatusCodes.NOT_FOUND.name,
                    message=settings.LOGIN_USER_NOT_FOUND,
                    idTransaction="",
                    data=[]
                ) 
            else:
                token_jwt = UtilsHelper.create_user_token()
                usuario = user.username
                return BaseResponseDTO(
                    code=StatusCodes.OK.value,
                    status=StatusCodes.OK.name,
                    message=settings.LOGIN_USER_SUCCESS,
                    idTransaction="",
                    data=[TokenResponses(token=token_jwt, username = usuario).serialize()]
                ) 
        except Exception as e:
            return BaseResponseDTO(
                code=StatusCodes.INTERNAL_SERVER_ERROR.value,
                status=StatusCodes.INTERNAL_SERVER_ERROR.name,
                message=str(e),
                idTransaction="",
                data=[Errors.HTTP_500_INTERNAL_SERVER_ERROR]
            ) 
        
    def recovery_password(self, correo: str, request: Request) -> list[UsersReponse]:
        try:
            token = UtilsHelper.create_user_token()
            print(token)
            user_db = self.repository.recovery_password(correo,token)
            if user_db is not None:
                file_email = templates.TemplateResponse("mailRecoveryPassword.html", {
                    'request': request,
                    'name_user': user_db.nombre+' '+user_db.apellido,
                    'hash': token,
                    'user_id': user_db.n_docu,
                    'client_url': settings.CLIENT_URL + settings.CLIENT_CONFIRM_RECOVERY_PASSWORD_ROUTE + str(user_db.n_docu) + '/' + token
                })
                
                file_email = file_email.body.decode("utf-8")
                text = """\
                    Confirmation mail
                    If you dont see the button below
                    Just press on the next link:
                    """ + settings.CLIENT_URL + settings.CLIENT_CONFIRM_RECOVERY_PASSWORD_ROUTE + """{}""".format(user_db.n_docu)+"""/{}
                    """.format(token)
                    
                is_sent_email = send_mail(
                    email=user_db.correo,
                    subject="Recovery Password",
                    body=file_email,
                    text=text,
                    cc=None
                )
                if is_sent_email:
                    return BaseResponseDTO(
                        code=StatusCodes.OK.value,
                        status=StatusCodes.OK.name,
                        message=settings.RECOVERY_PASSWORD_SUCCESS,
                        idTransaction="",
                        data=[]
                    )
                else:
                    return BaseResponseDTO(
                        code=StatusCodes.BAD_REQUEST.value,
                        status=StatusCodes.BAD_REQUEST.name,
                        message=settings.RECOVERY_PASSWORD_BAD_REQUEST,
                        idTransaction="",
                        data=[]
                    )
            else:
                return BaseResponseDTO(
                    code=StatusCodes.NOT_FOUND.value,
                    status=StatusCodes.NOT_FOUND.name,
                    message=settings.RECOVERY_PASSWORD_NOT_FOUND,
                    idTransaction="",
                    data=[]
                )
        except Exception as e:
            return BaseResponseDTO(
                code=StatusCodes.INTERNAL_SERVER_ERROR.value,
                status=StatusCodes.INTERNAL_SERVER_ERROR.name,
                message=str(e),
                idTransaction="",
                data=[Errors.HTTP_500_INTERNAL_SERVER_ERROR]
            )

        
    def confirm_recovery_password(self, id: int, token: str, password: str) -> list[UsersReponse]:
        try:
            user_db = self.repository.confirm_recovery_password(id, token, password)
            if user_db is not None:
                return BaseResponseDTO(
                    code=StatusCodes.OK.value,
                    status=StatusCodes.OK.name,
                    message=settings.CONFIRM_RECOVERY_PASSWORD_SUCCESS,
                    idTransaction="",
                    data=[]
                ) 
            else:
                return BaseResponseDTO(
                    code=StatusCodes.NOT_FOUND.value,
                    status=StatusCodes.NOT_FOUND.name,
                    message=settings.CONFIRM_RECOVERY_PASSWORD_NOT_FOUND,
                    idTransaction="",
                    data=[]
                ) 
        except Exception as e:
            return BaseResponseDTO(
                code=StatusCodes.INTERNAL_SERVER_ERROR.value,
                status=StatusCodes.INTERNAL_SERVER_ERROR.name,
                message=str(e),
                idTransaction="",
                data=[Errors.HTTP_500_INTERNAL_SERVER_ERROR]
            )