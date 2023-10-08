from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from app.common import settings, correlation_id_middleware, validation_exception_handler, exception_handler, Logger
from app.controller import auth

def create_app():
    # Configurar aplicación y Swagger
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        description=settings.DESCRIPTION_APP,
        version=settings.VERSION_APP,
        docs_url=settings.DOCS_URL
    )
       
    # Configurar CORS    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Configurar templates para renderizar vistas
    app.mount(settings.GET_STATIC_ROUTE, StaticFiles(directory="app/common/static"), name="static")
    
    # Añadir middlewares para procesar el request antes de llegar a las rutas del controlador
    app.middleware("http")(correlation_id_middleware)
    
    # Añadir prefijo a las rutas del controlador
    app.router.prefix = settings.API_V1_STR
    
    # Añadir capturadores de excepciones
    app.exception_handler(RequestValidationError)(validation_exception_handler)
    app.exception_handler(Exception)(exception_handler)
    
    # Añadir eventos de inicio y fin de la aplicación
    @app.on_event("startup")
    async def startup():
        Logger.get_logger(__name__).info("Starting up...")

    @app.on_event("shutdown")
    async def shutdown():
        Logger.get_logger(__name__).info("Shutting down...")
    
    # Añadir rutas del controlador
    app.include_router(auth)
    
    return app