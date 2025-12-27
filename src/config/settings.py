import os
from dotenv import load_dotenv

load_dotenv()



class Settings:
    ENV = os.getenv("CORA_ENV", "sandbox")
    CLIENT_ID = os.getenv("CORA_CLIENT_ID")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    BASE_URL = os.getenv("CORA_URL_PRODUCTION") if ENV == 'production' else os.getenv("CORA_URL_SANDBOX")

    CERT_PATH = os.path.join(BASE_DIR, "certs", ENV, "certificate.pem")
    KEY_PATH = os.path.join(BASE_DIR, "certs", ENV, "private-key.key")

settings = Settings()