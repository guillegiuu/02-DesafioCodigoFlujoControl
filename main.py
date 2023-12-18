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


# Operador == 
# Definicion:

"""
Como puedes ver en este código de solución, comparar dos cadenas en python se puede hacer utilizando el operador ==.

El operador == realiza una comparación estricta entre dos valores. Si ambos operandos tiene el mismo valor, el resultado de la comparación es True. Si los valores son de diferente tipo, el valor de la comparación es False.

"""

# C Siempre Falso: 

"""
Hay algunas situaciones que normalmente querrá evitar cuando programe utilizando sentencias condicionales. Un ejemplo es una contradicción. Esto ocurre cuando tu condición siempre será falsa sin importar el valor que le pases. Vamos a crear un ejemplo de una función que contiene una contradicción.

1 - Defina la función para que acepte un único parámetro llamado num.

2 - Utilice una combinación de <, > y y para crear una contradicción en una sentencia if.

3 - Si la condición es verdadera, devuelve True, en caso contrario devuelve False. El truco aquí es que como hemos escrito una contradicción, la condición nunca debería ser verdadera, así que deberíamos esperar devolver siempre False.

"""
def siempre_falso(num):
    if (num > 0 and num < 0):
        return True
    else:
        return False
print(siempre_falso(20))

# C.1 
def siempre_falso_1(num):
    num = 20
    if (num > 0 and num < 0):
        return True
    else:
        return False
print(siempre_falso_1(250))

"""
Se está verificando si "num" es mayor que cero y al mismo tiempo menor que cero, lo cual es imposible, ya que un número no puede ser mayor y menor que cero al mismo tiempo.

"""


