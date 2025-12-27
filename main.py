from fastapi import FastAPI, HTTPException
from src.model.schemas import PedidoBoleto
from src.services.boleto_service import BoletoService


app = FastAPI(title="Integração Cora")

service = BoletoService()

@app.get("/")
def health_check():
  return {
        "status": "online", 
        "service": "Cora Integration API", 
        "version": "1.0.0"
    } 

@app.get("/boletos")
def listar_boletos():
    return service.listar_boletos()

@app.post("/boletos", status_code=201)
def criar_boleto(pedido: PedidoBoleto):
    """
    Cria um boleto do 'Plano Basic'.
    Requer apenas dados do cliente e data de vencimento.
    Valor e Multas são aplicados automaticamente.
    """
    
    dados_entrada = pedido.dict()
    
    
    resultado = service.criar_boleto_fixo(dados_entrada)
    
    if resultado is None:
        raise HTTPException(status_code=400, detail="Não foi possível registrar o boleto na Cora.")
    
    return resultado