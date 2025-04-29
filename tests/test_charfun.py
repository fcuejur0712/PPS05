import unittest
#from app.scripts.charfun import esPalindromo
import random
import string
from unidecode import unidecode

# Funcion para comprobar la cadena
def esPalindromo(cadena:str) -> bool:
    
    # Pasar la cadena a minúsculas y eliminar los espacios
    cadena_sin_espacios = (cadena.lower()).replace(" ", "")
    # Convertir los caracteres especiales a caracteres unicode
    cadena_formateada = unidecode(cadena_sin_espacios)

    # La función devuelve un booleano haciendo uso de la técnica "slicing" para darle la vuelta a la cadena
    return cadena_formateada == cadena_formateada[::-1]

def generar_palindromo():
    mitad = "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(1,10)))
    return mitad + mitad[::-1]

class TestEsPalindromo(unittest.TestCase):
    def test_palindromo_simple(self):
        self.assertTrue(esPalindromo("anilina"))