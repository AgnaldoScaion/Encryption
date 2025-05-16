
# 🔐 Text Encryptor & Decryptor | Encriptador de Texto com Python

Este é um projeto simples, porém funcional, de **criptografia de arquivos de texto** feito em Python usando a biblioteca `cryptography`. Ele permite proteger informações sensíveis em um arquivo com criptografia simétrica — fácil de usar, ideal para aprendizado e pequenas aplicações.

This is a simple yet functional **text file encryption project** made in Python using the `cryptography` library. It allows you to protect sensitive data using symmetric encryption — beginner-friendly and useful for small tasks.

---

## 📌 Funcionalidades | Features

- 🔑 Geração de chave criptográfica (`Keyger.py`)
- 🔒 Criptografia de arquivos (`Encrypt.py`)
- 🔓 Descriptografia de arquivos (`Decrypt.py`)
- 🛠️ Script `main.py` para backup/restauração de todas as funções

---

## ⚙️ Como usar | How to Use

### ✅ Português — Passo a passo

1. **Instale a biblioteca necessária**:
   ```bash
   pip install cryptography
   ```

2. **Gere uma chave criptográfica**:
   - Execute o script `Keyger.py` uma vez.
   - Isso criará o arquivo `chave.key`.

3. **Crie um arquivo `dados.txt`** com o conteúdo que deseja proteger.

4. **Para criptografar**:
   - Execute o script `Encrypt.py`.
   - O conteúdo de `dados.txt` será criptografado automaticamente.

5. **Para descriptografar**:
   - Execute o script `Decrypt.py`.
   - O conteúdo original será restaurado no mesmo arquivo.

6. **(Opcional)** Use `main.py` como painel de controle e backup geral. Ele contém todas as funções.

---

### ✅ English — Step-by-step

1. **Install the required library**:
   ```bash
   pip install cryptography
   ```

2. **Generate an encryption key**:
   - Run the `Keyger.py` script once.
   - This will create the `chave.key` file.

3. **Create a file named `dados.txt`** with the text you want to secure.

4. **To encrypt**:
   - Run the `Encrypt.py` script.
   - The content of `dados.txt` will be encrypted.

5. **To decrypt**:
   - Run the `Decrypt.py` script.
   - The original content will be restored in the same file.

6. **(Optional)** Use `main.py` as a control panel and full-featured backup. It includes all functions.

---

## 📁 Estrutura do Projeto | Project Structure

```
.
├── Keyger.py         # Gera chave criptográfica / Generates encryption key
├── Encrypt.py        # Criptografa dados / Encrypts data
├── Decrypt.py        # Descriptografa dados / Decrypts data
├── main.py           # Backup completo com todas as funções / Full backup with all features
├── dados.txt         # Arquivo a ser criptografado / File to be encrypted
├── chave.key         # Arquivo de chave gerada / Generated key file
```

---

## 👨‍💻 Feito por / Made by

**Agnaldo** — Um projeto simples para estudar segurança de dados e criptografia em Python.

A simple project to explore basic data security and encryption in Python.

---

> Sinta-se à vontade para clonar, usar e modificar.  
> Feel free to clone, use, and modify.
