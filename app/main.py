from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routers.auth_router import router as auth_router
from app.api.routers.labels_router import router as labels_router
from app.api.routers.notes_router import router as notes_router
from app.api.routers.shares_router import router as shares_router
from app.core.db import init_db

load_dotenv()

#manejador de ciclo de vida
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db() #inicializa la base de datos
    yield

app = FastAPI(
    title =  settings.PROJECT_NAME,
    lifespan=lifespan, #registramos el ciclo de vida de la aplicacion
    swagger_ui_parameters={"persistAuthorization": True}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(notes_router, prefix="/api/v1")
app.include_router(labels_router, prefix="/api/v1")
app.include_router(shares_router, prefix="/api/v1")