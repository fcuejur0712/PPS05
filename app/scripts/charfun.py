# Título: charfun
# Autor: Fernando Cuenca
# Fecha de creación: 14-11-2024
# Descripción: programar la función "esPalindromo" y pedir al usuario la cadena de entrada

# Importar liberia que permite normalizar las cadenas
from unidecode import unidecode

# Funcion para comprobar la cadena
def esPalindromo(cadena:str) -> bool:
    
    # Pasar la cadena a minúsculas y eliminar los espacios
    cadena_sin_espacios = (cadena.lower()).replace(" ", "")
    # Convertir los caracteres especiales a caracteres unicode
    cadena_formateada = unidecode(cadena_sin_espacios)

    # La función devuelve un booleano haciendo uso de la técnica "slicing" para darle la vuelta a la cadena
    return cadena_formateada == cadena_formateada[::-1]

# Función que controla el flujo del programa solicitando la cadena al usuario
def ejecucion() -> None:

    # Solicitar la cadena al usuario
    cadena_usuario = input("Introduzca la cadena que desea comprobar que es palíndroma: ")

    while not str(cadena_usuario):
        cadena_usuario = input("Lo siento, el valor introducido no es válido, debes introducir una cadena: ")

    # Condicional donde se llama a la función y en función de si devuelve True o False da una respuesta al usuario
    if esPalindromo(cadena=cadena_usuario):
        print(f"La cadena '{cadena_usuario}' SI es palíndroma")
    else:
        print(f"La cadena '{cadena_usuario}' NO es palíndroma")

# Llamada a la función para la ejecución el programa
# ejecucion()