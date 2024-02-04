import math

def main_01(cord01: tuple, cord2: tuple):
    """
    Reciba las coordenadas `(x1, y1), (x2, y2)` de dos puntos del usuario e imprima la distancia entre los dos puntos de la siguiente manera.
    Para hacer esto, implemente la función `distancia(x1, y1, x2, y2)`.
    *Pauta de código:* consulte la fórmula para encontrar la distancia entre dos puntos.
    """
    
    if len(cord01) > 2 or len(cord2) > 2:
       raise ValueError("The class expect a (2) bi-dimentional tuple, and more than two dimention vector was provided.")
    
    return math.sqrt( (cord2[0] - cord01[0])**2  + (cord2[1] - cord01[1])**2 )

# print("Distances result: ", main_01((1,3) , (7,6)) )

def is_palindrome(cadena : str):
    """
    ## Q 18-01
    Un palíndromo es una oración, palabra o cadena que es lo mismo que leer cualquier carácter de forma consecutiva.

    Por ejemplo, hay palabras como level, kayak, salas, somos, radar, reconocer.

    Usemos una llamada recursiva para determinar el palíndromo.

    Defina una función llamada `is_palindrome` y escriba un programa que reciba una cadena del usuario e imprima 
    si el palindrome es correcto o no.

    **Pauta de código:** Llame a la función `is_palindrome` dentro de la función `is_palindrome`
    """
    if cadena == '':
        return False
    
    if cadena == cadena[::-1]:
        return True
    else:
        return False
       
#print( is_palindrome("level") )

## With AI help:

def is_palindrome_AI(text):
    """
        This function checks if a given string is a palindrome using recursion.

        Args:
            text: The string to check.

        Returns:
            True if the string is a palindrome, False otherwise.
    """

    # Base case: If the string is empty or has only one character, it's a palindrome.
    if len(text) <= 1:
        return True

    # Recursive case: Check if the first and last characters are the same,
    # and then check the remaining substring recursively.
    return text[0] == text[-1] and is_palindrome_AI(text[1:-1])

# Example usage
text = "racecar"
if is_palindrome_AI(text):
  print(f"{text} is a palindrome.")
else:
  print(f"{text} is not a palindrome.")



def main_03():
    """
    ## Q 19-01
    Después de poner una lista llamada `n_list` con valores de `[10, 20, 30]` en la función `map`.

    ```
    n_list = [10,20,30]
    twice  = list(map(lambda x: x*2, n_list))
    triple = list(map(lambda x: x*3, n_list))
    ```

    Indique el contenido de las variables `twice` y `triple`.
    """
    print("Content of function: ", "twice must be", [20,40,60])
    print("Content of function: ", "triple must be", [30,60,90])

#main_03()

"""
## Q 20-01
En el siguiente código, espere qué valor se incluye finalmente en `num_list`. Calcule el resultado esperado a mano.
**Pauta de codificación:** Escriba 5 veces la declaración `for`. Espere este resultado y envíe el resultado.

def calc_digit(n): 
   def findal(digit):
      return digit**n
   return findal

num_list = []

for num in range(1,6):
    num_list.append( calc_digit(num) )
    print( num_list[num-1](num) )

#Expected values:
 [1*1, 2*2, 3*3, 4*4, 5*5]
"""

def main_05():
    print("""
    ## Q 21-01

    Implemente las funciones de multiplicación (*) y división (/) de dos vectores usando los métodos `mul` y `truediv` aprendidos 
    en la **unidad 21**. Suponiendo que `v1` es `(30, 40)` y `v2` es `(10, 20)`, codifique (escriba la declaración de salida) para 
    devolver el siguiente resultado como resultado de la multiplicación y división de dos vectores.

    **Pauta de codificación:** escriba código que amplíe la funcionalidad de la clase `Vector2D` que aprendió en este capítulo.
    """)


class Vector2D:
    
    __coords = (0, 0)
    
    def __init__(self, coordinates: tuple):
        if len(coordinates) > 2 or type(coordinates) != tuple:
            raise ValueError("The class expect a (2) bi-dimentional tuple, and more than two dimention vector was provided.")
        self.__coords = coordinates
        
    def get_scalar(self):
        return math.sqrt( self.__coords[0]**2 + self.__coords[1]**2 )
    
    def __truediv__(self, vector2d):
        """
        Why can't we divide a vector?
        Originally Answered: Why can't we divide the vector? Since a vector quantity had both magnitude as well as direction, though magnitudes can be easily divided to get a fixed value, dividing directions is meaningless.
        """
        return self.get_scalar() / vector2d.get_scalar()
    
    def __mul__(self, vector2d):
       return Vector2D((self.__coords[0]*vector2d.__coords[0], self.__coords[1]*vector2d.__coords[1]))

    
v1 = Vector2D((30, 40)) 
v2 = Vector2D((10, 20))

print("Vector magnitud division: ", v1 / v2)
print("Vector mulplication, a new vector ", v1 * v2)