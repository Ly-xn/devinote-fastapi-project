from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL") #Es un valor requerido y se obtiene desde el archivo .env
    JWT_SECRET: str = Field(..., env="JWT_SECRET") 
    JWT_ALG: str = Field(default = "HS256", env="JWT_ALG") #Algoritmo de encriptacion por defecto es HS256
    JWT_EXPIRES_MIN: int = Field(default = 60*24, env="JWT_EXPIRES_MIN") #Tiempo de expiracion del token por defecto es 1 dia
    PROJECT_NAME: str = "Devinote " #Nombre del proyecto por defecto es FastAPI

    class Config:
        env_file = ".env" #Archivo de configuracion por defecto es .env

settings = Settings() 