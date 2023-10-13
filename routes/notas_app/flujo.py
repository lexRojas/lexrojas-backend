from fastapi import APIRouter
from config.db  import conn

flujo = APIRouter()

@flujo.post("/flujo")
async def setFlujo(valor:int):
      with conn.cursor() as cursor:
        # Read a single record
        if ( valor > 0):
          sql = f"INSERT INTO flujo (valor) VALUES ({valor});"
          print (sql) 
          i = cursor.execute(sql)
          print (i)
          conn.commit
      return {"message": "Employee added successfully"}



@flujo.get("/flujo")
async def getFlujo():
      with conn.cursor() as cursor:
        # Read a single record
        sql = f"SELECT * FROM  flujo;"
        cursor.execute(sql)
        result = cursor.fetchall
        return result 