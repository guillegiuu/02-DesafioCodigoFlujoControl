import os

print("Hello world from ...")
os.system("python --version")

# A En Rango:
"""
Empecemos los problemas avanzados probando si un número está dentro de un cierto rango. Aceptaremos tres parámetros donde el primer parámetro es el número que estamos probando, el segundo parámetro es el límite inferior y el tercer parámetro es el límite superior de nuestro rango. Estos son los pasos necesarios:

1 - Defina la función para que acepte tres números como parámetros.

2 - Comprobar si el número es mayor o igual que el límite inferior y menor o igual que el límite superior.

3 - Si es cierto, devuelve True, en caso contrario, devuelve False.


"""


def en_rango(num, inferior, superior):
    if (num >= inferior and num <= superior):
        return True
    else:
        return False


print(en_rango(5, 1, 10))  # True
print(en_rango(5, 6, 10))  # False

# Operador AND:
# Definicion:
"""
Devuelve True si ambas condiciones son verdaderas y False en cualquier otro caso.

El operador and realiza una evaluación perezosa (short-circuiting), lo que significa que si la primera condición es falsa, la segunda ni siquiera se evalúa, ya que el resultado general será False independientemente del valor de la segunda condición. 

"""

# B Mismo nombre:
"""
Necesitamos escribir un programa que compruebe diferentes nombres y determine si son iguales. Necesitamos aceptar dos cadenas (strings) y compararlas. Aquí están los pasos:

1 - Define la función para que acepte dos cadenas, tu_nombre y mi_nombre.

2 - Comprueba si las dos cadenas son iguales.

3 - Devuelve True si son iguales, en caso contrario devuelve False.


"""


def mismo_nombre(tu_nombre, mi_nombre):
    if (tu_nombre == mi_nombre):
        return True
    else:
        return False


print(mismo_nombre("guille", "manu"))
print(mismo_nombre("rober", "rober"))
