from sqlmodel import SQLModel, Field


#Esta clase funciona como modelo de bases de datos
class User(SQLModel, table=True): #Al crear la clase user heredamos de SQLModel y ya viene SQLalchemy y Pydantic
    id: int = Field(default=None, primary_key = True)
    email: str = Field(index = True, unique = True)
    full_name: str = Field(default="")
    hashed_password: str

#Este es el validor o mapa que yo quiero recibir para crear un usuario
class UserCreate(SQLModel):
    email: str
    full_name: str = ""
    password: str

#Clase validadora para sacar informacion del usuario
class UserRead(SQLModel):
    id: int 
    email: str
    full_name: str
    model_config = {"from_attributes": True} 