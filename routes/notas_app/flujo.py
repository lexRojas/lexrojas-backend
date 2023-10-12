from fastapi import APIRouter
from config.db  import conn

flujo = APIRouter();

@flujo.post("/flujo",)
async def setFlujo(valor:int):
      with conn.cursor() as cursor:
        # Read a single record
        if ( valor > 0):
          sql = "insert into flujo values ({valor})" 
        cursor.execute(sql)
