import os
from dotenv import load_dotenv
from pydantic import BaseSettings
from app.common.helper.utilsHelper import helper as UtilsHelper

load_dotenv()

class Config:
    DATABASE_PASSWORD: str = UtilsHelper.decrypt_data(os.getenv("DATABASE_PASSWORD"))
    DATABASE_SERVER: str = UtilsHelper.decrypt_data(os.getenv("DATABASE_SERVER"))
    DATABASE_USER: str = UtilsHelper.decrypt_data(os.getenv("DATABASE_USER"))
    DATABASE_NAME: str = UtilsHelper.decrypt_data(os.getenv("DATABASE_NAME"))
    DATABASE_PORT: str = UtilsHelper.decrypt_data(os.getenv("DATABASE_PORT"))

    DATABASE_URL: str = f"mysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_NAME}"