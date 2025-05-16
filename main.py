# Para executar o código, você deve ter o módulo `cryptography` instalado. 
# Você pode instalá-lo usando o seguinte comando:
# pip install cryptography

# Agora para executar, basta ir no Keyger.py e executar o código para gerar a chave.
# Crie caso não tenha o arquivo chave.key.
# Após, crie o dados.txt com o conteúdo que você deseja criptografar.
# E basta executar o Encrypt.py para criptografar o arquivo.
# Caso queira descriptografar, basta executar o Decrypt.py.

# E é isto :D
# Ambos arquivos feitos pelo Agnaldo :D

# To run the code, you must have the `cryptography` module installed.
# You can install it using the following command:
# pip install cryptography

# To start, run Keyger.py to generate the key.
# Do this if the chave.key file does not already exist.
# Then, create a file called dados.txt with the content you want to encrypt.
# Run Encrypt.py to encrypt the file.
# If you want to decrypt it later, simply run Decrypt.py.

# And that’s it :D
# All files created by Agnaldo :D

#                           _______   
#                          | ___  o|  
#                          |[_-_]_ |  
#       ______________     |[_____]|  
#      |.------------.|    |[_____]|  
#      ||            ||    |[====o]|  
#      ||            ||    |[_.--_]|  
#      ||            ||    |[_____]|  
#      ||            ||    |      :|  
#      ||____________||    |      :|  
#  .==.|""  ......    |.==.|      :|  
#  |::| '-.________.-' |::||      :|  
#  |''|  (__________)-.|''||______:|  
#  `""`_.............._\""`______     
#     /:::::::::::'':::\`;'-.-.  `\   
#    /::=========.:.-::"\ \ \--\   \  
#    \`""""""""""""""""`/  \ \__)   \ 
#     `""""""""""""""""`    '========'


# ========================
#      BACKUP COMPLETO
#    FULL CODE BACKUP
# ========================

from cryptography.fernet import Fernet

# Gera uma nova chave e salva no arquivo 'chave.key'
# Generates a new key and saves it to 'chave.key'
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)
    print("Chave gerada com sucesso! / Key generated successfully!")

# Criptografa o conteúdo de 'dados.txt'
# Encrypts the content of 'dados.txt'
def criptografar_arquivo():
    try:
        with open("chave.key", "rb") as chave_arquivo:
            chave = chave_arquivo.read()
        fernet = Fernet(chave)

        with open("dados.txt", "rb") as arquivo:
            conteudo = arquivo.read()

        criptografado = fernet.encrypt(conteudo)

        with open("dados.txt", "wb") as arquivo:
            arquivo.write(criptografado)

        print("Arquivo criptografado com sucesso! / File encrypted successfully!")
    except Exception as e:
        print("Erro ao criptografar / Error while encrypting:", e)

# Descriptografa o conteúdo de 'dados.txt'
# Decrypts the content of 'dados.txt'
def descriptografar_arquivo():
    try:
        with open("chave.key", "rb") as chave_arquivo:
            chave = chave_arquivo.read()
        fernet = Fernet(chave)

        with open("dados.txt", "rb") as arquivo:
            conteudo = arquivo.read()

        descriptografado = fernet.decrypt(conteudo)

        with open("dados.txt", "wb") as arquivo:
            arquivo.write(descriptografado)

        print("Arquivo descriptografado com sucesso! / File decrypted successfully!")
    except Exception as e:
        print("Erro ao descriptografar / Error while decrypting:", e)