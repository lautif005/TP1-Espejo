from fastapi import APIRouter, Query, status
from . import schemas, services

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=schemas.ClienteRead, status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente: schemas.ClienteCreate):
    return services.crear_cliente(cliente)

@router.get("/", response_model=list[schemas.ClienteRead])
def listar_clientes(
    ciudad: str | None = Query(None, description="Filtrar por ciudad"),
    activo: bool | None = Query(None, description="Filtrar por estado activo/inactivo")
):
    return services.obtener_clientes(ciudad=ciudad, activo=activo)

@router.get("/{cliente_id}", response_model=schemas.ClienteRead)
def obtener_cliente(cliente_id: int):
    return services.obtener_cliente(cliente_id)