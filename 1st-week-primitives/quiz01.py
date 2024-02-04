import random

"""
Edwin Roman
Rep. Dominicana
"""

"""
## Q 01-01

El código que imprime los valores numéricos del 1 al 3 utilizando la función `print()` es `print(1+2+3)`.
Con referencia a este código, imprima los valores de 1 a 5 de forma similar.
"""
def q_01():
    print("1+2+3+4+5")

''' 
## Q 02-01
Un programa que calcula la suma de números impares entre enteros entre 1 y 100 e imprime el resultado.
Completa los espacios en blanco de la segunda figura del siguiente diagrama de flujo.
'''

def q_02():
    _sum = 0
    
    for num in range(100):
        if(num % 2 == 0):
            _sum += 1 
    
    print("Evens numbers: ", _sum)
    
''' 
## Q 03-01

El Código para imprimir la siguiente salida decorativa.

Utilice sólo un carácter '*' en la primera línea y use el operador * y número. 

En la segunda línea, utilice sólo un carácter '#' y un espacio, y utilice el operador * y el número.

**Guía de codificación:**

- En el caso de la primera línea, imprima de la misma manera que '*' * número n.

- La segunda línea también utiliza el operador.
'''

def q_03():
    num01 = int(input("Numero 1:"))
    num02 = int(input("Numero 2:"))
    
    print("Number of:",num01," *")
    print("*"*num01)
    
    print("Number of:",num01," #")
    print("#"*num02)
    
#q_03()

''' 
## Q 04-01

Escribe y guarda tu nombre y dirección en las variables nombre y dirección, respectivamente.

Escribe un código que lo imprima en la pantalla de la siguiente manera.

**Guía de codificación:** Utiliza una variable como `nombre = 'Mi nombre'`.

**Respuesta:**
'''

def q_04():
    nombre : str = input("Nombre: ")
    direccion : str = input("Write down your address: ")
    
    print("Mi nombre es:" , nombre, ", direccion es", direccion)

#q_04()

''' 
## Q 05-01 - Espere el resultado del siguiente código y escríbalo.
'''

def q_05():
    x = 1 
    y = 0
    print(x and y) # return 0
    print(x or y)  # return 1
    print(not x)   # return False
    print(not y)   # return True

#q_05()

''' 
## Q 06-01

Escriba un programa que tome dos enteros aleatorios como entrada y los enumere de menor a mayor.

(Restricción: dos enteros distintos, es decir, que no sean el mismo número)

**Pauta de codificación:**
- Reciba la entrada del usuario con la función de entrada y conviértala en un número entero usando la función `int`.
- Luego, use una declaración `if` para comparar e imprimir los dos valores.

**Respuesta:**
'''

def q_06():
    num01 = int(input("Inserte el 1er numero:"))
    num02 = int(input("Inserte el 2do numero:"))

    if(num02 == num01):
        print("No puede ser números iguales.")

    print([2,1].sort())
    
#q_06()


''' 
## Q 07-01

Escriba un programa que realice las siguientes funciones utilizando una expresión condicional compuesta de una sentencia `if`.

**Guía de codificación:**
- Escriba un código que se ejecute de forma diferente dependiendo de si la respuesta a la primera pregunta es 0 o 1.

¿Eres un adulto? (1 si es mayor de edad, 0 si es menor de edad): 1
¿Está casado? (1 si es casado, 0 si es soltero): 1
Usted es un adulto que está casado.

Las tres salidas posibles son:
- Usted es un adulto que está casado.
- Usted es un adulto que está soltero.
- Usted es menor de edad.

**Respuesta:**
'''
def q_07() -> None:
    
    is_single = 1 if input("Are you single? y\\n ") == "y"  else 0
    is_mayor = 1 if input("Are you law old? y\\n ") == "y" else 0

    if(is_mayor and is_single):
        print("Usted es un adulto que está soltero.")
    elif(is_mayor and not is_single):
        print("Usted es un adulto que está casado.")
    else:
        print("Usted es un menor de edad")

#q_07()


''' 
## Q 08-01

Entre los números naturales positivos distintos del 1, un número que no es primo se llama número compuesto. 
Escribe los números primos y compuestos del 2 al 12 de la siguiente manera.

**Pauta de codificación:**
- use la instrucción `for` para resolver este problema.
- Cuando se utiliza una instrucción `for` anidada, se debe usar una expresión para determinar un número primo en el lazo `for` interno.
'''

def q_08():
    for x in range(2, 13):
        if x%2 :
            print("Primo :",x)
        else:
            print("Compuesto :",x)
#q_08()

''' 
## Q 09-01

Un número de Armstrong es un número entero de tres dígitos que es igual a la suma de los cubos de cada dígito.

Encuentre todos los números de Armstrong entre enteros de tres dígitos e imprímalos de la siguiente manera.

**Pauta de codificación:** todos los números del 100 al 999 deben buscarse utilizando la instrucción `for`.

**Respuesta:**
'''

def is_armstrong(str_num : str) -> int:
    """ Si retorna 0, indica que no es un número Armstrong, de lo contrario retornará el número en sí. """
    
    armstrog_num = 0
    
    if not str_num.isdigit():
        return 0
    
    for x in str_num:
        armstrog_num += int(x)**len(str_num)
    
    return int(str_num) if armstrog_num == int(str_num) else 0  

def q_09() -> None:
    armstrong_list = []
    
    for x in range(100, 1000):
        num = is_armstrong(x.__str__()) 
        if num != 0:
           armstrong_list.append(num)
    
    print("Resulted armstrong numbers:", armstrong_list)
    
q_09()