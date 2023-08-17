from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.actos import actos
from routes.registros import registros


app = FastAPI()

origins = [
    "https://localhost:3000",
    "https://mylextools-d3b8930fee26.herokuapp.com/",
    "mylextools-d3b8930fee26.herokuapp.com/"
]


app.add_middlewareeware ( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}

app.include_router(registros)
app.include_router(actos)


