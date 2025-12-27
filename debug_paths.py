import os
import sys

# Adiciona o diretório atual ao path para garantir que encontramos o src
sys.path.append(os.getcwd())

from src.config.settings import settings

def verificar_caminhos():
    print("-" * 50)
    print("DIAGNÓSTICO DE CAMINHOS")
    print("-" * 50)
    
    # 1. Verificar BASE_DIR
    print(f"1. Diretório Base do Projeto (BASE_DIR):")
    print(f"   -> {settings.BASE_DIR}")
    
    # 2. Verificar Caminho do Certificado
    print(f"\n2. Caminho calculado para o CERTIFICADO:")
    print(f"   -> {settings.CERT_PATH}")
    if os.path.exists(settings.CERT_PATH):
        print("   [OK] O arquivo existe!")
    else:
        print("   [ERRO] O arquivo NÃO foi encontrado neste local.")
        
    # 3. Verificar Caminho da Chave
    print(f"\n3. Caminho calculado para a CHAVE:")
    print(f"   -> {settings.KEY_PATH}")
    if os.path.exists(settings.KEY_PATH):
        print("   [OK] O arquivo existe!")
    else:
        print("   [ERRO] O arquivo NÃO foi encontrado neste local.")
    
    # 4. Listar conteúdo da pasta de certificados (se a pasta existir)
    pasta_certs = os.path.dirname(settings.CERT_PATH)
    print(f"\n4. Conteúdo da pasta {pasta_certs}:")
    if os.path.exists(pasta_certs):
        arquivos = os.listdir(pasta_certs)
        for arq in arquivos:
            print(f"   - {arq}")
    else:
        print("   [ERRO] A pasta de certificados nem sequer existe.")

    print("-" * 50)

if __name__ == "__main__":
    verificar_caminhos()