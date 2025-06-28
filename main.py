from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.user_routes import router as user_router

app = FastAPI(
    title="Sistema de Gestión de Usuarios",
    description="API para registrar, consultar y gestionar usuarios en la plataforma.",
    version="1.0.0",
)

@app.get("/", response_class=HTMLResponse, tags=["Inicio"])
async def root():
    return """
    <html>
        <head>
            <title>Bienvenido</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f4f4f4; text-align: center; padding: 50px; }
                h1 { color: #333; }
                p { color: #666; }
                a { color: #007bff; text-decoration: none; }
            </style>
        </head>
        <body>
            <h1>Bienvenido al Sistema de Gestión de Usuarios</h1>
            <p>Esta es una API construida con FastAPI.</p>
            <p>Explora la documentación en <a href="/docs">/docs</a></p>
        </body>
    </html>
    """

app.include_router(user_router)
