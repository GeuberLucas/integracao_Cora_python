import uuid
from src.core.api_client import CoraClient

class BoletoService:
    def __init__(self):
        self.client = CoraClient()

    
    
    DADOS_FIXOS = {
        "service_template": {
            "name": "Plano Basic - Datameros",
            "description": "Licença de uso do sistema",
            "amount": 9900, 
        },
        
        "discount_template": {
            "type": "PERCENT",
            "value": 10
        },
        "payment_forms": ["BANK_SLIP", "PIX"]
    }

    def listar_boletos(self):
        """Lista os boletos da conta."""
        endpoint = "/v2/invoices"
        try:
            response = self.client.get(endpoint)
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            print(f"Erro: {e}")
            return None

    def criar_boleto_fixo(self, dados_entrada):
        """
        Recebe apenas o Cliente e Data, e monta o payload completo
        com os valores fixos.
        """
        endpoint = "/v2/invoices"
        
        
        codigo_boleto = dados_entrada.get("code") or str(uuid.uuid4())
        vencimento = dados_entrada["due_date"]
        
        
        if hasattr(vencimento, 'isoformat'):
            vencimento_str = vencimento.isoformat()
        else:
            vencimento_str = str(vencimento)
        
        payload_final = {
            "code": codigo_boleto,
            "customer": dados_entrada["customer"], 
            "services": [
                self.DADOS_FIXOS["service_template"] 
            ],
            "payment_terms": {
                "due_date": vencimento_str, 
                "discount": self.DADOS_FIXOS["discount_template"] 
            },
            "payment_forms": self.DADOS_FIXOS["payment_forms"] 
        }

        print(f"Payload Montado: {payload_final}") 

        
        try:
            
            response = self.client.post(endpoint, payload_final, idempotency_key=codigo_boleto)
            
            if response.status_code in [200, 201]:
                return response.json()
            else:
                print(f"Erro Cora: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            print(f"Erro Crítico: {e}")
            return None