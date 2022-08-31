from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Cliente(BaseModel):
    codigo: int = None
    nome: str
    cpf: str
    telefone: str
    compra_fiado: int = None
    dia_fiado: int
    senha: str = None

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE
@router.get("/cliente/{id}", tags=["cliente"])
def get_Cliente(id: int):
    return {"msg": "get executado", "id": id}, 200
@router.post("/cliente/{id}", tags=["cliente"])
def post_Cliente(id: int, f: Cliente):
    return {"msg": "post executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}, 200
@router.put("/cliente/{id}", tags=["cliente"])
def put_Cliente(id: int, f: Cliente):
    return {"msg": "put executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}, 201
@router.delete("/cliente/{id}", tags=["cliente"])
def delete_Cliente(id: int):
    return {"msg": "delete executado", "id": id}, 201