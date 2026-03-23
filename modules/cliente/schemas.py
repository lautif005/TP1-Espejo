from pydantic import BaseModel, Field

class ClienteBase(BaseModel):
    nombre: str = Field(..., min_length=3, description="Nombre del cliente")
    email: str = Field(..., description="Correo electrónico del cliente")
    ciudad: str | None = None
    activo: bool = True

class ClienteCreate(ClienteBase):
    pass

class ClienteRead(ClienteBase):
    id: int