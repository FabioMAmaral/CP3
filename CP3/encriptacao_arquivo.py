from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def save_key_to_file(key, filename='encryption_key.key'):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key_from_file(filename='encryption_key.key'):
    with open(filename, 'rb') as f:
        key = f.read()
    return key

def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(filename + '.encrypted', 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(encrypted_filename, key):
    fernet = Fernet(key)

    with open(encrypted_filename, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_filename = os.path.splitext(encrypted_filename)[0]
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

encryption_key = generate_key()
save_key_to_file(encryption_key)
filename = 'arquivo.txt'

encrypt_file(filename, encryption_key)
print("Arquivo encriptado com sucesso!")

encrypted_filename = filename + '.encrypted'
password = input("Digite a senha para descriptografar o arquivo: ")

password_encoded = password.encode()
key = load_key_from_file()
decrypt_file(encrypted_filename, key)
