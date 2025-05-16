# Criptografa o conteúdo de 'dados.txt' usando a chave gerada em 'chave.key'
# O arquivo original será sobrescrito com o conteúdo criptografado

# Encrypts the content of 'dados.txt' using the key from 'chave.key'
# The original file will be overwritten with the encrypted content

from cryptography.fernet import Fernet

# Lê a chave de criptografia
# Reads the encryption key
with open("chave.key", "rb") as chave_arquivo:
    chave = chave_arquivo.read()

fernet = Fernet(chave)

# Lê o conteúdo do arquivo a ser criptografado
# Reads the file to encrypt
with open("dados.txt", "rb") as arquivo:
    conteudo = arquivo.read()

# Criptografa o conteúdo
# Encrypts the content
criptografado = fernet.encrypt(conteudo)

# Salva o conteúdo criptografado de volta no arquivo
# Saves the encrypted content back to the file
with open("dados.txt", "wb") as arquivo:
    arquivo.write(criptografado)

print("Arquivo criptografado com sucesso! / File encrypted successfully!")
