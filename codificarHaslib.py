import hashlib

# A mensagem que você deseja "criptografar"
mensagem = "Olá, mundo!".encode()

# Criar um hash da mensagem
hash_object = hashlib.sha256(mensagem)
hex_dig = hash_object.hexdigest()

print("Texto cifrado:", hex_dig)
