from typing import Iterator
from sqlmodel import SQLModel, Session, create_engine
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True, connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}) #Crea el motor de la base de datos

def init_db() -> None:
    pass
    #SQLModel.metadata.create_all(engine) #unicamente para dev

def get_session() -> Iterator[Session]:
    """
    No devuelve un valor unico, sino que produce uno o mas objetos de Session.
    """
    with Session(engine) as session:
        #Crea una nueva sesion de sqlmodel vinculada al engine y la gestiona como un contex manager
        #Cuando el contexto termina, la sesion se cierra automaticamente
        yield session
