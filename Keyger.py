# Gerador de chave de criptografia
# Execute este arquivo uma vez para gerar o arquivo 'chave.key'

# Encryption key generator
# Run this file once to create the 'chave.key' file

from cryptography.fernet import Fernet

chave = Fernet.generate_key()

with open("chave.key", "wb") as chave_arquivo:
    chave_arquivo.write(chave)

print("Chave gerada com sucesso! / Key generated successfully!")
