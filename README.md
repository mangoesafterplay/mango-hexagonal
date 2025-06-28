# Sistema de Gestión de Usuarios

Este proyecto implementa una API REST para registrar, consultar y gestionar usuarios en una plataforma. Está desarrollado con **FastAPI**, **SQLAlchemy asíncrono** y sigue una arquitectura **hexagonal (ports & adapters)**, separando claramente el dominio, los casos de uso y la infraestructura.

---

## Características principales

- Arquitectura hexagonal: desacopla dominio, casos de uso y persistencia.
- FastAPI para endpoints HTTP con documentación automática Swagger.
- SQLAlchemy (async) con PostgreSQL (Neon) para consultas no bloqueantes.
- Hash seguro de contraseñas con bcrypt.
- Migraciones de base de datos con Alembic.

---

## Cómo iniciar el proyecto

1. **Clona el repositorio**
    ```bash
    git clone https://github.com/mangoesafterplay/mango-hexagonal.git
    cd mango-hexagonal
    ```

2. **Instala dependencias**
    ```bash
    python -m venv venv
    source venv/bin/activate    #Para Linux
    venv\Scripts\activate       #Para Windows
    pip install -r requirements.txt
    ```

3. **Configura el entorno**
    - Copia el archivo `.env.example` a `.env` y coloca tus credenciales de base de datos.

4. **Ejecuta las migraciones**
    ```bash
    alembic upgrade head
    ```

5. **Levanta el servidor**
    ```bash
    uvicorn main:app --reload
    ```

6. Abre en tu navegador:
    - Documentación Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠 Roadmap / Futuras mejoras

- ✅ Autenticación con JWT.
- ✅ Pruebas unitarias (pytest).
- ✅ CI/CD con GitHub Actions.

