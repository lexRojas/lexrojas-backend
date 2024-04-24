from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.notario.actos import actos
from routes.notario.registros import registros
from routes.notas_app.estudiante import estudiante
from routes.notas_app.notas import notas
from routes.notas_app.calendario import calendario
from routes.notas_app.flujo import flujo
from routes.notario.indice import indice

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(registros)
app.include_router(actos)
app.include_router(estudiante)
app.include_router(notas)
app.include_router(calendario)
app.include_router(flujo)
app.include_router(indice)

