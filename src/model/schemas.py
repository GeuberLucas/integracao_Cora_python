from datetime import date
from pydantic import BaseModel
from typing import Optional


class Documento(BaseModel):
    identity: str
    type: str  


class Cliente(BaseModel):
    name: str
    email: str
    document: Documento



class PedidoBoleto(BaseModel):
    customer: Cliente
    due_date: date 
    code: Optional[str] = None 