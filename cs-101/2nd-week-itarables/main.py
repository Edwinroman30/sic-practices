"""
# Actividad: Creación de una Base de Datos en Python

## Descripción

A continuación debes crear una base de datos simple utilizando listas en Python. Una base de datos es una colección de datos organizados que se utilizan para almacenar y recuperar información. En este caso, simularemos una base de datos de estudiantes con información básica.

## Instrucciones

1. Crea un programa en Python que permita a los usuarios realizar las siguientes acciones:

   a. Agregar un nuevo estudiante a la base de datos. Cada estudiante debe tener al menos un nombre, un número de identificación y una edad. Puedes utilizar una lista para almacenar estos datos.

   b. Mostrar la lista de estudiantes en la base de datos.

   c. Buscar un estudiante por su número de identificación y mostrar su información.

   d. Actualizar la información de un estudiante existente en la base de datos.

   e. Eliminar un estudiante de la base de datos.

2. Utiliza listas de Python para almacenar la información de los estudiantes. Por ejemplo, puedes crear una lista de diccionarios, donde cada diccionario representa un estudiante con sus datos.

3. Ofrece un menú interactivo que permita a los usuarios elegir las acciones que desean realizar en la base de datos.

4. Implementa la lógica necesaria para cada acción, como agregar, buscar, actualizar o eliminar estudiantes.

## Ejemplo de Base de Datos

A continuación, se muestra un ejemplo de cómo podría verse una base de datos de estudiantes utilizando listas y diccionarios:

Desarrolle el código en la siguiente lista.
"""
from os import system
import platform
import json

def main_01():

    base_de_datos = [
        {"nombre": "Juan", "id": 1, "edad": 20},
        {"nombre": "María", "id": 2, "edad": 22},
        {"nombre": "Carlos", "id": 3, "edad": 21}
    ]

    is_still_alive = True
    option = 0


    def clear_terminal():
        if platform.system() == "Windows":
            system("cls")
        else:
            system("clear")

    def print_menu(): 
        print("""
            Menu:
            -----------------------------------------------------------------------------------
            (1). Agregar un nuevo estudiante a la base de datos. 
            (2). Mostrar la lista de estudiantes en la base de datos.
            (3). Buscar un estudiante por su número de identificación y mostrar su información.
            (4). Actualizar la información de un estudiante existente en la base de datos.
            (5). Eliminar un estudiante de la base de datos.
            (6). Limpiar la consola.
            """)

    def add_student(student_db : list):
        student = {}
        student["id"] = len(student_db) + 1
        student["nombre"] = input("Introduzca su nombre:")
        student["edad"] = int(input("Introduzca su edad:"))

        student_db.append(student)
        
    def get_student_by_id(_id : int, student_db : list):
        student : dict = list( filter( lambda x : x["id"] == _id, student_db) )[0]
        print(student)

    def update_student(_id : int, student_db : list):
        
        new_name = input("Introduzca el nuevo nombre:")
        new_age = input("Introduzca la nueva edad:")

        student : dict = list( filter( lambda x : x["id"] == _id, student_db) )[0]
        student["nombre"] = new_name
        student["edad"] =  int(new_age) if new_age.isdigit() else student["edad"]
        
        print("Listo, valor actualizado...")
        #student_db = list( filter( lambda student : student["id"] != _id, student_db) )

    def delete_student(_id : int, student_db : list):
        newlist : list = []
        
        for data in student_db:
           if data["id"] != _id:
             newlist.append(data)
        
        student_db.clear()
        student_db.extend( newlist ) 
        
    print_menu()
    while (is_still_alive):
    
        option = int( input("Elija una opcion:") )
        
        if option == 1:
            add_student(base_de_datos)
        elif option == 2:
            print("Los estudiantes registrados son: \n", base_de_datos)
        elif option == 3:
            identifier = input("Inserte el Id del estudiante:")
            if identifier.isdigit():
                get_student_by_id( int(identifier) , base_de_datos )
            else:
                print("Usted introdujo un Id que no es valido a buscar...")
        elif option == 4:
            identifier = input("Inserte el Id del estudiante:")
            if identifier.isdigit():
                update_student( int(identifier), base_de_datos )
            else:
                print("Usted introdujo un Id que no es valido a buscar...")
        elif option == 5:
            identifier = input("Inserte el Id del estudiante:")
            if identifier.isdigit():
                delete_student( int(identifier), base_de_datos )
            else:
                print("Usted introdujo un Id que no es valido a buscar...")
        elif option == 6:
            clear_terminal()
        else:
            print("La opcion que ha seleccionado esta fuera de rango...")
            is_still_alive = False
            break

        print_menu()

#main_01()

def main_02():
    # Espacio para desarrollar las pruebas, si tienes alguna duda o comentario adicional
    # lo puedes dejar planteado acá.

    list_notas = [15, 21, 24, 40, 13, 14, 18, 17, 14.5]
    
    #list_notas[START_INDEX: END_INDEX : STEP]
    """
    START = Posicion donde inician la busqueda.
    END = Posicion donde termina la busqueda.
    STEP = Saltos de busquedas.
    """
    #list_notas[::2]
    
    print(list_notas[::2])
    
#main_02()

def main_03():
    """
    ### Actividad: Crear diccionarios y guardarlos como archivo JSON.
    De la unidad 11 sección 4.6 revise el ejemplo mostrado.
    Genera un diccionario, sobre la información que deseas guardar como base de datos, desarrollo el código necesario para generar el 
    archivo JSON, y también el código para cargar la información del archivo JSON.
    """
    try:
        employemment_data = {
            "name": "Edwin Roman",
            "age" : 239,
            "skills" : ("Good Communication", "Self-drive", "UI/UX Figma", ".NET", "Docker"),
            "url" : "https://github.com/Edwinroman30",        
        }
        
        filename = "info.json"
        
        with open(f"{filename}","w") as _file :
            json.dump(employemment_data, _file, indent= "\t")
        
        print("File and data created...")
    except:
        print("Error no pudimos procesar la data...")
    
#main_03()

def main_04():
    # Espacio para desarrollar el código siguiendo las instrucciones.
    tup = (1, 2, 3, 4, 5)

    # (1)
    # Las tuplas son inmutables, una vez creadas sus valores no pueden ser modificadas.
    # Las lista en su defecto son mutables, pueden cambiar y son elementos de referencias ReferenceType.

    # (2) RGB
    my_favorite_color = (253, 34, 9)

    # (3)
    print( 3 in tup )
    
#main_04()

def main_05():
    # Espacio para desarrollar el código, escriba comentarias breves para explicar su funcionamiento.

    """
    Una lista bi-dimencional es aquella cuya composición esta dada por la integraci[on] de una lista sobre la otra siendo la lista contenedora tener de
    0 a N donde N es un numero entero :)
    """
    bidimension = [[2, 2, 3], [9, 0, 2]]
    suma = 0;

    for x in range( len(bidimension) ):
       for y in range( len(bidimension) ):
          print(bidimension[x][y])

    suma = sum(bidimension[0]) + sum(bidimension[1])
    print(suma) 

#main_05()


def main_06():
    """
    ### Actividad: Revision de los métodos usados en el manejo de diccionarios.
    ### Instrucciones

    1. Crear un diccionario.
    2. Testear los siguientes métodos para el majeo de diccionarios get(), keys(), values(), items(), pop(), clear()
    3. Agregar un breve comentario sobre su funcionamiento.
    """
    
    student = {
        "name" : "Edwin Roman",
        "country" : "Dominican Republic",
        "age" : None
    }
    
    print("get() - obtiene los valores de la clave especificada, contrario un error", student.get("name"))
    
    print("keys() -> Retorna las claves que componen el dict", student.keys())
    
    print("values() -> Retorna los valores que se encuentran asociados al diccionario en formato de lista.", student.values())
    
    print("items() -> Retorna los valores/cada valor key-value, en formato de dupla", student.items())
    
    print("pop() -> Elimina el key-valor registrado, identificando el mismo por el key proporcionado.", student.pop("age"))
    print(student)
    
    print("clear() -> Limpia todo el obj", student.clear())
    
main_06()