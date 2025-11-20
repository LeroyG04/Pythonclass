import hashlib

texto = input("Ingresa tu contraseña: ")
hashhex = hashlib.sha256(texto.encode()).hexdigest()
print("El hash es :", hashhex)
