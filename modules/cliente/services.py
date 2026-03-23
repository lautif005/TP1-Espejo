from fastapi import HTTPException
from .schemas import ClienteCreate

clientes_db = []
contador_id = 1

def obtener_clientes(ciudad: str | None = None, activo: bool | None = None) -> list[dict]:
    resultado = clientes_db
    if ciudad:
        resultado = [c for c in resultado if c.get("ciudad") and c.get("ciudad").lower() == ciudad.lower()]
    if activo is not None:
        resultado = [c for c in resultado if c.get("activo") == activo]
    return resultado

def crear_cliente(cliente_in: ClienteCreate) -> dict:
    global contador_id
    
    for c in clientes_db:
        if c["email"] == cliente_in.email:
            raise HTTPException(status_code=400, detail="El email ya está registrado en el sistema")
            
    nuevo_cliente = cliente_in.model_dump()
    nuevo_cliente["id"] = contador_id
    clientes_db.append(nuevo_cliente)
    
    contador_id += 1
    return nuevo_cliente

def obtener_cliente(cliente_id: int) -> dict:
    for c in clientes_db:
        if c["id"] == cliente_id:
            return c
    raise HTTPException(status_code=404, detail=f"Cliente con ID {cliente_id} no encontrado")