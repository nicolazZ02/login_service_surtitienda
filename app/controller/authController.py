from fastapi import APIRouter, Request
from app.common import settings, BaseResponseDTO, SessionLocal, Errors, ErrorModel, UtilsHelper, LogRoutes, StatusCodes
from app.service import AuthService
from app.controller.request.authRequest import LoginRequest,UserRecoveryPasswordRequest,UserPasswordRequest

auth = APIRouter()
auth.route_class = LogRoutes

db = SessionLocal()
service = AuthService(db)

# Endpoint para obtener todos los usuarios

@auth.get(
        settings.GET_ROL_BY_USERNAME_ROUTE,
        tags=["Login"], response_model= list[BaseResponseDTO],
        responses={
            Errors.HTTP_404_NOT_FOUND.status_code: {"model": ErrorModel, "description": settings.HTTP_404_NOT_FOUND["description"]},
            Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: {"model": ErrorModel, "description": settings.HTTP_500_INTERNAL_SERVER_ERROR["description"]}
        }
)
def get_rol_by_username(username: str, request: Request) -> list[BaseResponseDTO]:
    try:
        result = service.get_rol_by_username(username)
        result[0].idTransaction= UtilsHelper.get_correlation_id(request)
        return result
    except Exception as e:
        return [BaseResponseDTO(
            code=StatusCodes.INTERNAL_SERVER_ERROR.value,
            status=StatusCodes.INTERNAL_SERVER_ERROR.name,
            message=str(e),
            idTransaction=UtilsHelper.get_correlation_id(request),
            data=[Errors.HTTP_500_INTERNAL_SERVER_ERROR]
        )]

@auth.post(
    settings.LOGIN_ROUTE,
    tags=["Login"], response_model= BaseResponseDTO,
    responses={
        Errors.HTTP_404_NOT_FOUND.status_code: {"model": ErrorModel, "description": settings.HTTP_404_NOT_FOUND["description"]},
        Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: {"model": ErrorModel, "description": settings.HTTP_500_INTERNAL_SERVER_ERROR["description"]}
    }
)
def login(login: LoginRequest,request: Request) -> BaseResponseDTO:
    try:
        result = service.login_user(login)
        result.idTransaction = UtilsHelper.get_correlation_id(request)
        return result
    except Exception as e:
        return [BaseResponseDTO(
            code=StatusCodes.INTERNAL_SERVER_ERROR.value,
            status=StatusCodes.INTERNAL_SERVER_ERROR.name,
            message=str(e),
            idTransaction=UtilsHelper.create_user_token(request),
            data=[Errors.HTTP_500_INTERNAL_SERVER_ERROR]
        )]       

@auth.put(
    settings.PUT_CONFIRM_RECOVERY_PASSWORD_ROUTE,
    tags=["Recovery_Password"], response_model=BaseResponseDTO,
    responses={
        Errors.HTTP_400_BAD_REQUEST.status_code: {"model": ErrorModel, "description": settings.HTTP_400_BAD_REQUEST["description"]},
        Errors.HTTP_404_NOT_FOUND.status_code: {"model": ErrorModel, "description": settings.HTTP_404_NOT_FOUND["description"]},
        Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: {"model": ErrorModel, "description": settings.HTTP_500_INTERNAL_SERVER_ERROR["description"]}
    }
)
def confirm_recovery_password(id: int, token: str, password: UserPasswordRequest, request: Request) -> BaseResponseDTO:
    try:
        result = service.confirm_recovery_password(id, token, password.password)
        result.idTransaction = UtilsHelper.get_correlation_id(request)
        return result
    except Exception as e:
        return [BaseResponseDTO(
            code=StatusCodes.INTERNAL_SERVER_ERROR.value,
            status=StatusCodes.INTERNAL_SERVER_ERROR.name,
            message=str(e),
            idTransaction=UtilsHelper.get_correlation_id(request),
            data=[Errors.HTTP_500_INTERNAL_SERVER_ERROR]
        )]
    
@auth.post(
    settings.POST_RECOVERY_PASSWORD_ROUTE,
    tags=["Recovery_Password"], response_model=BaseResponseDTO,
    responses={
        Errors.HTTP_400_BAD_REQUEST.status_code: {"model": ErrorModel, "description": settings.HTTP_400_BAD_REQUEST["description"]},
        Errors.HTTP_404_NOT_FOUND.status_code: {"model": ErrorModel, "description": settings.HTTP_404_NOT_FOUND["description"]},
        Errors.HTTP_500_INTERNAL_SERVER_ERROR.status_code: {"model": ErrorModel, "description": settings.HTTP_500_INTERNAL_SERVER_ERROR["description"]}
    }
)
def recovery_password(correo: UserRecoveryPasswordRequest, request: Request) -> BaseResponseDTO:
    try:
        result = service.recovery_password(correo.correo, request)
        result.idTransaction = UtilsHelper.get_correlation_id(request)
        return result
    except Exception as e:
        return [BaseResponseDTO(
            code=StatusCodes.INTERNAL_SERVER_ERROR.value,
            status=StatusCodes.INTERNAL_SERVER_ERROR.name,
            message=str(e),
            idTransaction=UtilsHelper.get_correlation_id(request),
            data=[Errors.HTTP_500_INTERNAL_SERVER_ERROR]
        )]