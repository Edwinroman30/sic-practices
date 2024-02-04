# Edwin Roman, Secci[on] lunes a miercoles Rep. Dominicana

"""
## Q 10-01

Si hay dos listas `l1` y `l2` con las siguientes cadenas, use la combinación de `l1` y `l2` para imprimir de la siguiente manera.

**Pauta de codificación:** use bucles anidados e imprímalos.

```
l1 = ['I like','I love']
l1 = ['pancake.','kiwi juice.','espresso.']
```
"""

def main_01():
   l1 = ['I like','I love']
   l2 = ['pancake.','kiwi juice.','espresso.']
   
   for prefix in l1:
       for sufix in l2:
           print(prefix, sufix, sep=" ")

#main_01()


"""
## Q 11-01

El diccionario de personas se define de la siguiente manera.

Agregue un nuevo elemento a este diccionario de personas con la clave 'Padre' y el valor 'John Doe'.

**Pauta de codificación:** después de definir el diccionario de personas, escriba el código para agregar nuevos elementos.

`person = {'Name':'David Doe', 'Age':26, 'Weight':82, 'Job':'Data Scientist'}`
"""
def main_02():
    person = {'Name':'David Doe', 'Age':26, 'Weight':82, 'Job':'Data Scientist'}
    father_name = input(f"Instruzca el nombre del padre de {person['Name']}:\n")
    
    person['Father'] = father_name
    
    print(person)
    

#main_02()


"""
## Q 12-01

Al usar datos de tupla, los valores de dos variables se pueden intercambiar sin usar una variable temporal.
Usando este método de intercambio, escriba un programa que reemplace el valor más grande de 12 en la lista dada, 
y pase a la posicióndel último.

**Pauta de codificación:** use un bucle `for`. Al intercambiar valores en una lista, no se deben usar variables adicionales como temp.

`lista = [5,6,3,9,2,12,3,8,7]`
"""

def main_03():
    lista = [5,6,3,9,2,12,3,8,7]
    is_sorted = False
    
    while(not is_sorted):
        is_sorted = True
        for x in range(len(lista) - 1):
            if lista[x] > lista[x + 1]:
                lista[x], lista[x + 1] = lista[x + 1], lista[x]
                is_sorted = False
    
    print("Sorted list using Bubble Sort:\n", lista)
    


#main_03()


"""
## Q 13-01

La matriz bidimensional `a` contiene los valores `[[1, 2], [3, 4], [5, 6]]`.

Cambie esta matriz bidimensional a una matriz unidimensional como `[1, 2, 3, 4, 5, 6]` e imprímala.

**Pauta de codificación:** use un bucle `for`. Defina una nueva matriz y coloque los elementos de a en esta matriz.
"""

def main_04():
    bidimentional = [[1, 2], [3, 4], [5, 6]]
    single_list = []
    
    for a in bidimentional:
        single_list.extend(a)

    print(single_list)
    
#main_04()



"""
## Q 14-01

Dada un diccionario en la variable **maria** que contiene las puntuaciones de los cursos 
'coreano', 'inglés', 'matemáticas' y 'ciencia', se almacenan como clave:valor. Imprima el 
puntaje promedio para los puntajes de las asignaturas de maría.

**Guía de codificación:** Utilice los métodos de diccionario **values()** y **len()** funciones.

`maria = { 'korean':94, 'english':91, 'maths':89, 'science':83 }`
"""

def main_05():
    maria = { 'korean':94, 'english':91, 'maths':89, 'science':83 }
    result = 0
    
    for val in maria.values():
        result += val
    
    print("The average is: ", (result/len(maria)))
    

#main_05()



"""
## Q 15-01

Declare una variable `school` con un diccionario anidado de la siguiente manera.

```
school = {
    'kim':{ 'age':16, 'hei':170, grade:3 },
    'lee':{ 'age':15, 'hei':165, grade:2 },
    'cho':{ 'age':14, 'hei':167, grade:1 },
}
```

Luego, use la función `deepcopy()` del módulo de copia para escribir un programa que 'copie' a otra variable, `school2`. 
(Verifique que `school` y `school2` sean variables diferentes a través del operador `is`).

**Pauta de codificación:** Imprima el resultado de `school is school2`, que debe ser falso.
"""
from copy import deepcopy

def main_06():
    
    school = {
    'kim':{ 'age':16, 'hei':170, "grade":3 },
    'lee':{ 'age':15, 'hei':165, "grade":2 },
    'cho':{ 'age':14, 'hei':167, "grade":1 },}
    
    #school2 = dict(school)
    school2 = deepcopy(school)
    
    print("Is it the first equal to the second? ", school is school2)
    

#main_06()




def main_07():
    scores = (
    ('DongKyu Park' , 88, 95, 90),
    ('YoungMin Kang', 85, 90, 95),
    ('DongMin Park' , 70, 90, 80),
    ('Seungloo Hong', 90, 90, 95),)

    zipped_math_tuple = list(zip( scores[0], scores[1], scores[2], scores[3] ))[2]
    
    print("Math course grades average", sum(zipped_math_tuple) / len(zipped_math_tuple) )
    
    
#main_07()

def main_09():
    
    def divisible(n):
        ''' def divisible_n(x):
            return x%n == 0

        return divisible_n '''
        
        return lambda x: x%n == 0 

    esDivisiblePor2 = divisible(2)
    esDivisiblePor7 = divisible(7)

    print(esDivisiblePor2(6))
    print(esDivisiblePor7(22))
        
    
    # Funciones que devuelven funciones
#main_09()

def saludar(nombre, hora):
    
  # SALUDAR SCOPE
  def dia(nombre):
    print("¡Buenos días", nombre + "!")
  def noche(nombre):
    print("¡Buenas noches", nombre + "!")
  def tarde(nombre):
    print("¡Buenas tardes", nombre + "!")
  def manana(nombre):
    print("¡Hola! ¿Cómo amaneciste", nombre + "?")
  
  if hora <= 11: manana(nombre)
  elif hora <= 14: dia(nombre)
  elif hora <= 19: tarde(nombre)
  else: noche(nombre)



def decorador(funcion):
    
  def empotrar_f(*args, **kwargs): # Transformamos la función a una versión decorada
    print("Empecé a hacer algo")
    funcion(*args, **kwargs)
    print("Terminé de hacer algo")

  return empotrar_f # Devolvemos la función con una versión decorada

saludar_decorado = decorador(saludar)

saludar_decorado("Vivian", 13)

class Circle():
    PI = 3.14
    
    def __init__(self, radio = 0):
        self.radio = radio

    def __str__(self):
        return "Representation..."
        

obj = Circle()

print(obj)