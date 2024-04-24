from fastapi import APIRouter
from config.db  import conn
from pydantic import BaseModel
from datetime import date
from config.classes import quincena

indice = APIRouter()

@indice.get("/indice")
async def getIndice(valor:quincena):
      with conn.cursor() as cursor:
        # Read a single record
        # if not valor:
        print(valor)
        sql = "select * from valores_usuales" 
        # else:
        #   sql = "select * from valores_usuales where fecha between '2024-03-15' and '2024-03-31'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return(result)

