from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect
# from models.user import User

app = FastAPI()


connect(db="LinguasII", host="mongodb+srv://liviagcarvalho:12345@cluster.sfj2axl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster")

# Permitir conexão com o React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"message": "API da Linguas2 rodando com sucesso!"}
