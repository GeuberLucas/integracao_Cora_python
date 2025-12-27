import uuid
import requests
from src.config.settings import settings

class CoraClient:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.cert = (settings.CERT_PATH, settings.KEY_PATH)
        self.token = None
        
    def authenticate(self):
        """Obtém o token de acesso usando o Client ID e os certificados."""
        url = f"{self.base_url}/token"
        
        payload = {
            "grant_type": "client_credentials",
            "client_id": settings.CLIENT_ID
        }
        
        try:
            response = requests.post(url, data=payload, cert=self.cert)
            response.raise_for_status() 
            
            data = response.json()
            self.token = data.get("access_token")
            print("Autenticação realizada com sucesso!")
            
        except requests.exceptions.RequestException as e:
            print(f"Erro na autenticação: {e}")
            if response:
                print(f"Detalhe: {response.text}")

    def get_headers(self):
        """Gera os cabeçalhos com o Token de autorização."""
        if not self.token:
            self.authenticate()
        
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        """Método genérico para fazer GET"""
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=self.get_headers(), cert=self.cert)

    def post(self, endpoint, data,idempotency_key=None):
        """Método genérico para fazer POST"""
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key
        else:
            headers["Idempotency-Key"] = str(uuid.uuid4())
        return requests.post(url, json=data, headers=headers, cert=self.cert)