# 📝 Devinotes API

**Devinotes** es una API RESTful inspirada en la aplicación de Google Keep construida con **FastAPI** para la gestión de notas personales. Este proyecto fue desarrollado como parte de un curso intensivo de Backend con Python, implementando las mejores prácticas de desarrollo moderno.

## 🚀 Características Principales

- **Gestión de Notas (CRUD):** Crear, Leer, Actualizar y Eliminar notas.
- **Validación de Datos:** Uso de **Pydantic** para asegurar la integridad de la información.
- **Base de Datos:** Persistencia de datos utilizando **SQLModel** (compatible con SQLite y PostgreSQL).
- **Documentación Interactiva:** Swagger UI y ReDoc integrados automáticamente.

## 🛠️ Tecnologías Utilizadas

- **Python 3.12.10**
- **FastAPI** (Framework web)
- **SQLModel** (ORM & Base de datos)
- **Render** (Desplegado)

## Endpoints principales:

| Método | Endpoint | Descripción
| :--- | :--- | :--- |
| `POST` | `/auth/register` | El usuario crea una cuenta. |
| `POST` | `/auth/login` | El usuario inicia sesion con su cuenta. |
| `POST` | `/auth/login` | El usuario inicia sesion con su cuenta usando Swagger. |
| `GET` | `/labels` | Devuelve una lista con todas las etiquetas. |
| `POST` | `/labels` | Crea una etiqueta. |
| `DELETE` | `/labels/{label_id}` | Elimina una etiqueta. |
| `GET` | `/notes` | Devuelve una lista con todas las notas. |
| `POST` | `/notes` | Crea una nota. |
| `PATCH` | `/notes/{note_id}` | Crea una nota. |
| `DELETE` | `/notes/{note_id}` | Elimina una nota. |
| `POST` | `/shares/notes/{note_id}` | Comparte una nota. |
| `DELETE` | `/shares/notes/{note_id}` | Elimina una nota compartida. |
| `POST` | `/shares/labels/{label_id}` | Comparte una etiqueta. |
| `DELETE` | `/shares/labels/{label_id}` | Elimina una etiqueta compartida. |


## ⚙️ Instalación y Ejecución

### 1 - Clonar el repositorio:
 
- git clone [https://github.com/Ly-xn/devinote-fastapi-project.git](https://github.com/Ly-xn/devinote-fastapi-project.git)
- cd devinote-fastapi-project

### 2 - Crear y activar entorno virtual:

- python -m venv venv
## En Windows:
- venv\Scripts\activate
## En Mac/Linux:
- source venv/bin/activate

### 3 - Instalar dependencias:

- pip install -r requirements.txt

### 4 - Correr el servidor:

- fastapi dev main.py