from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from config.db  import conn


flujo = APIRouter()

# Pydantic model to define the schema of the data
class Flujo(BaseModel):
    idFlujo: int
    fecha: datetime
    valor: int

# Route to create an item
@flujo.post("/flujo/", )
async def create_item(v:int):
    cursor = conn.cursor()
    query = f'INSERT INTO flujo (valor) VALUES ({v});'
    cursor.execute(query)
    conn.commit()
    i = cursor.lastrowid
    cursor.close()
    return i

# Route to read an item
@flujo.get("/flujo" )
async def read_item():
    with conn.cursor() as cursor:
      query = "SELECT * FROM flujo;"
      cursor.execute(query)
      items = cursor.fetchall()
      return (items)
