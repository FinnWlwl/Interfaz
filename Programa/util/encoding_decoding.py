#============================================================================================================#
#                         FUNCIONES DE CIFRADO Y DESCIFRADO DE CONTRASEÑAS                                   #
#============================================================================================================#
"""
Descripción:
Este archivo proporciona funciones para encriptar y desencriptar contraseñas.
Utiliza una clave estática compartida con el algoritmo Fernet (de la librería cryptography)
para proteger las contraseñas de forma segura mediante cifrado simétrico.
"""

#============================================================================================================#
#                                   IMPORTACIÓN DE LIBRERÍAS                                                 #
#============================================================================================================#
from cryptography.fernet import Fernet  # Cifrado simétrico seguro y fácil de usar

#============================================================================================================#
#                                      CLAVE DE CIFRADO FIJA                                                 #
#============================================================================================================#
KEY = b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g='  # Clave fija utilizada para cifrar y descifrar

#============================================================================================================#
#                            FUNCIONES DE ENCRIPTACIÓN Y DESENCRIPTACIÓN                                     #
#============================================================================================================#
def encrypted(password: str) -> str:  # Encripta una contraseña y la retorna como cadena en base64
    f = Fernet(KEY)  # Crea un objeto Fernet usando la clave definida
    encrypted_password = f.encrypt(password.encode('utf-8'))  # Convierte la contraseña a bytes y la encripta
    return encrypted_password.decode('utf-8')  # Devuelve el resultado en formato string

def decrypt(token: str) -> str:  # Desencripta una cadena cifrada y la devuelve como texto plano
    try:
        f = Fernet(KEY)  # Crea un objeto Fernet con la misma clave
        decrypted_password = f.decrypt(token.encode('utf-8'))  # Convierte el token a bytes y lo desencripta
        return decrypted_password.decode('utf-8')  # Devuelve la contraseña original como string
    except Exception as e:
        print(f"Error al desencriptar: {e}")  # Muestra un mensaje de error si algo falla
        return None  # Retorna None si ocurre una excepción

#============================================================================================================#
#                                   PRUEBA DE FUNCIONAMIENTO (OPCIONAL)                                      #
#============================================================================================================#
# pw = "contraseña123"  # Contraseña original
# token = encrypted(pw)  # Encripta la contraseña
# print("Token:", token)  # Muestra el token cifrado

# pw_dec = decrypt(token)  # Desencripta el token
# print("Desencriptado:", pw_dec)  # Muestra la contraseña original recuperada
