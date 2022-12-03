from fastapi import FastAPI
from server.routes.pessoa import router as PessoaRouter


app = FastAPI()

app.include_router(PessoaRouter, tags=['Pessoa'], prefix='/pessoa')


@app.get('/', tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
