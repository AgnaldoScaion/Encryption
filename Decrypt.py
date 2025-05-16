# Descriptografa o conteúdo de 'dados.txt' usando a chave gerada em 'chave.key'
# O arquivo será sobrescrito com o conteúdo original em texto plano

# Decrypts the content of 'dados.txt' using the key from 'chave.key'
# The file will be overwritten with the original plain text content

from cryptography.fernet import Fernet

# Lê a chave de criptografia
# Reads the encryption key
with open("chave.key", "rb") as chave_arquivo:
    chave = chave_arquivo.read()

fernet = Fernet(chave)

# Lê o conteúdo criptografado do arquivo
# Reads the encrypted content from the file
with open("dados.txt", "rb") as arquivo:
    conteudo = arquivo.read()

# Descriptografa o conteúdo
# Decrypts the content
descriptografado = fernet.decrypt(conteudo)

# Salva o conteúdo descriptografado de volta no arquivo
# Saves the decrypted content back to the file
with open("dados.txt", "wb") as arquivo:
    arquivo.write(descriptografado)

print("Arquivo descriptografado com sucesso! / File decrypted successfully!")
