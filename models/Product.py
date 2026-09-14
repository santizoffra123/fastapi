from pydantic import BaseModel


class Producto(BaseModel):
    nombre: str
    stock: int
    precio: float