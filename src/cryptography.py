#Creando llave semilla
def generate_key(seed):
    key = seed + 255 #Con lo que generamos la semilla
    return key

#Creando la tabla de llaves
def creating_key_table(seed, keys_num):
    key_table = []
    for i in range(keys_num):
        key = generate_key(seed +i)
        key_table.append(key)
    return key_table

#Mensaje cifrado entre cada caracter y la llave
def encrypt(message,key):
    encrypted = ""
    for char in message:
        encrypted += chr(ord(char) ^ (key & 0xFF))
    return encrypted

#Para descifrar mensaje
def decrypt(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        decrypted += chr(ord(char) ^ (key & 0xFF))
    return decrypted

#Comunicación entre nodos

def main():
    #Semilla compartida
    seed = 654321

    #Generando llave
    keys_num = 5
    key_table = creating_key_table(seed, keys_num)
    key = key_table[0] #Se selecciona esta llave

    #Mensaje original
    message = "Probando Mensaje"

    #Cifrado (nodo emisor)
    encrypted_message = encrypt(message, key)

    #Descifrado (nodo receptor)
    decrypted_message = decrypt(encrypted_message, key)

    print("Tabla de llaves: ", key_table)
    print("Mensaje original: ", message)
    print("Mensaje cifrado: ", [ord(c) for c in encrypted_message])
    print("Mensaje descifrado: ", decrypted_message)

#Para el programa
if __name__ == "__main__":
    main()