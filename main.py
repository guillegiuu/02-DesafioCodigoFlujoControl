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

# D Reseña de Pelicula:
"""
Queremos crear una función que nos ayude a calificar películas. Nuestra función dividirá las calificaciones en diferentes rangos y le dirá al usuario cómo fue la película basándose en la calificación de la película. 

1 - Define nuestra funcion que acepte un unico numero llamado valoracion "rating".

2 - Si la valoracion es igual o inferior a 5, devuelve "Terrible!".

3 - Si la calificacion es inferior a 9, devuelve "Interesante".

4 - Si no se cumple ninguna de las condiciones anteriores, devuelve "Increible!".

"""


def reseña_pelicula(rating):
    if (rating <= 5):
        return "Terrible!"
    elif (rating > 5 and rating < 9):
        return "Interesante"
    else:  # Mayor a 9
        return "Increible!"


print(reseña_pelicula(9))  # "Increible!"
print(reseña_pelicula(6))  # "Terrible!"
print(reseña_pelicula(3))  # "Terrible!"
"""
Este código define una función llamada reseña_pelicula que toma un parámetro llamado rating. Dentro de la función, comprueba el valor de rating para determinar la reseña de la película. Si la calificación es menor o igual a 5, entonces devuelve "¡Terrible!". Si la calificación es mayor que 5 y menor que 9, devuelve "Interesante". Si la calificación no cumple las condiciones anteriores (calificación mayor o igual a 9), devuelve "¡Increíble!". A continuación, se llama a la función tres veces con valoraciones diferentes (9, 6 y 3) y se imprimen los resultados en la consola.
"""

# E Numero Maximo:
"""

Para el reto final, vamos a seleccionar qué número de tres valores de entrada es el mayor utilizando sentencias condicionales. Para ello, tenemos que comprobar las diferentes combinaciones de valores para ver qué número es mayor que los otros dos. 

1 - Defina una función que tenga tres parámetros de entrada, num1, num2 y num3.

2 - Comprueba si num1 es mayor que los otros dos números.
3 - En caso afirmativo, devuelve num1.

4 - Comprueba si num2 es mayor que los otros dos números.
5 - Si es así, devuelve num2.

6 - Comprueba si num3 es mayor que los otros dos números.
7 - Si es así, devuelve num3.

8 - Si hubiera un empate entre los dos números mayores, entonces devuelve "¡Es un empate!".


"""


def max_num(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num1 and num2 > num3):
        return num2
    elif (num3 > num1 and num3 > num2):
        return num3
    else:
        return "¡Es un empate!"


print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))
"""

Este código define una función llamada max_num que recibe tres parámetros: num1, num2 y num3. Compara estos tres números para averiguar cuál es el mayor. Esto es lo que ocurre dentro de la función:

Primero comprueba si num1 es mayor que num2 y num3. Si esto es cierto, devuelve num1, ya que es el número mayor.
Si la primera condición no es cierta, comprueba si num2 es mayor que num1 y num3. Si se cumple, devuelve num2, ya que es el número mayor.
Si ninguna de estas condiciones es cierta, comprueba si num3 es mayor que num1 y num2. Si es cierto, devuelve num3, ya que es el número mayor.
Si no se cumple ninguna de estas condiciones, significa que al menos dos números son iguales y el tercero es menor. En este caso, devuelve "¡Es un empate!", que significa "¡Es un empate!".
Después de definir la función, se llama con varios conjuntos de números para probar la función. Por ejemplo, max_num(-10, 0, 10) devuelve 10, ya que 10 es el mayor número de este conjunto.

"""
