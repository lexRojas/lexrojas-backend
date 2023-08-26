from fastapi import APIRouter
from config.db  import conn

notas = APIRouter();

@notas.get("/notas")
async def getNotas(id = "-1", idMateria="1"):
      with conn.cursor() as cursor:
        # Read a single record
        if (id=="-1"):
          sql = "select * from notas" 
        else:
          sql = "SELECT * FROM  notas n inner join estudiante e on e.id = n.id where e.id ="+ str(id) + " and n.idMateria = " + str(idMateria)
        cursor.execute(sql)
        result = cursor.fetchall()
        return(result)