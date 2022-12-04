from fastapi import FastAPI
from .routes.pieces import router as PieceRouter


app = FastAPI()

app.include_router(PieceRouter, tags=["Piece"], prefix="/piece")


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@app.get("/hello")
async def get_hello():
    return {"message": "Hello World"}
