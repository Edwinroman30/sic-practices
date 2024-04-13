def main():
    """2.- Diseñe una solución que determine si una cadena de paréntesis, llaves y corchetes
    es válida. Ejemplo:"""
    #Entrada: (){[]()}
    #Salida: Válido

    #Fuente de: https://www.youtube.com/watch?v=RZatXgHAPKY
    
    def cadena_validator(chain_input: str ) -> bool:
        
        parentheses_simbols = { "(" : ")",  "{" : "}",  "[" : "]"  }
        stack = []

        for chart in chain_input:
            
            if( chart in parentheses_simbols.keys() ):
                stack.append(chart)
            elif ( len(stack) == 0 or chart != parentheses_simbols.get( stack.pop() ) ) : #Este ultimo cierre, es el tuyo? si, pues ok sigue que no hay problemas.
                return False

        return len(stack) == 0 # Puede no quede alguno abierto lo que quiere decir que es valida o puede que quede alguno al que nunca encontro cerradura

    print( cadena_validator("()[{}") )
    
#main()

def main_01():
    """
     # Generar un código para revisar los nombres contenidos en la lista, y guardarlos en diferentes listas,
     # de acuerdo a la inicial del nombre, use los comandos usandos antenirmente y barra los elementos usando 
     # el comando "for nombre in nombres_aleatorios:" al final del proceso la lista inicial debe quedar vacia.
    """
    stack = []
    nombres_aleatorios = ["Ana", "Carlos", "David", "Elena", "Fernando", "Gabriela",
                      "Hugo", "Isabel", "Juan", "Luis", "Lucía",
                      "Lorena", "Manuel", "María", "Miguel", "Natalia",
                      "Nicolás", "Nora", "Óscar", "Olivia", "Pablo", "Paula",
                      "Pedro", "Raquel", "Rafael", "Renata", "Roberto", "Rosario",
                      "Sara", "Sergio", "Silvia", "Tomás", "Teresa", "Víctor", "Verónica",
                      "Ximena", "Xavier", "Yolanda", "Yenny", "Zaira", "Zoe", "Zacarías"]
    
    for nombre in nombres_aleatorios:
        stack.append(nombre[0])
    
    non_duplicated = list( set(stack) )
    
    print("Print of the #1st lettler contented into this list:", non_duplicated)
    
    stack = []
    for nombre in nombres_aleatorios:
            stack.append(nombre)
    
    print("Stack lenght", len(stack))
        
#main_01()

def main_02():
    # Actividad: Replique el código, mostrado en la presentación 36 correspondiente al capítulo 4.
    """
    En este codódigo se muestra la creación de una clasa para crear una pila y hacer las actividades básicas correspondientes.

    - **__init__**: Creación de la pila.
    - **is_empty**: Verificación si la pila está vacia.
    - **push**: agregar elemento a la pila
    - **pop**:si la pila no está vacia eliminar el último de elemento.

    Use la notación mostrada en la presentacion 40, realice varias operaciones y comente brevemente los resultados (máximo 3 lineas), antes de pasar a la siguiente actividad asegurese de entender completamente la notación utilizada.
    """
    class Stack():
        def __init__(self) -> None:
            self.internal_stack = []
        
        def is_empty(self) -> bool:
            return True if len(self.internal_stack) == 0 else False
        
        def push(self, item: any):
            self.internal_stack.append(item)
            return item
        
        def pop(self):
            return None if self.is_empty() else self.internal_stack.pop()
    
    ''' Ejecucion y explicacion '''
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push("3")
    
    print(my_stack.pop(), my_stack.pop())
    # En este caso se la clase funciona como una estructura Stack (LIFO)
    # en este ejemplo se puede evidenciar porque el [ultimo] elemento insertado es el primero en visualizarse y asi sucesivamente.
    # insertando (1,2,3) obtuve (3,2,1 y en caso de None)

#main_02()
 
def main_03():
    """
    ### Actividad: Búsqueda secuencial.
    Se tiene una lista de 10 ciudades organizadas en función de la densidad de población, escriba una función para retornar la posición ocupada.
    """
    
    ciudades = [
        "Daca, Bangladés",
        "Karachi, Pakistán",
        "Nueva Delhi, India",
        "Manila, Filipinas",
        "Seúl, Corea del Sur",
        "Cantón, China",
        "Taipéi, Taiwán",
        "Chenaral, Chile",
        "Shenzhen, China",
        "Bombay, India"
    ]

    def obtener_posicion(ciudades: list, ciudad: str):
        # Espaciós para desarrollar el código      
        # return ciudades.index(ciudad)
        
        for inx, city in enumerate(ciudades):
            if city == ciudad:
                return inx       

    posicion_ocupada = obtener_posicion(ciudades,"Seúl, Corea del Sur")
    print("Posicion ocupada: ",posicion_ocupada)
 
#main_03()     

def main_04():
    """
    ### Actividad: Búsqueda binaria.
    - Escriba al menos una ventaja de la busqueda binaria.
    - Replique el código mostrado en la presentación 192.
    - Explique brevemente el funcionamiento del código, maximo 3 lineas.
    - Ingrese un piso de ruptura del huevo y calcule cuantas veces se realiza la revisión para encontrar el piso seguro.
      (Se puede agrear algún contador dentro del código para verificar)
    """
    
    # Espacio para replicar el código.

    # Espacio para explicar funcionamiento.

    # Cálculo y verificación del número de veces que se realiza la verificación.


main_04()


