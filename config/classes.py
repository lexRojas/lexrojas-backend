from pydantic import BaseModel

class quincena(BaseModel):
    fecha_inicio:str
    fecha_final:str