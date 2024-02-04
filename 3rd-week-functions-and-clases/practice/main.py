def main_01():
    """
    # Actividad: Creacion de funciones.
        ## Instrucciones

        1. Defina en forma breve el concepto de función.
            Respuesta: Una función es un elemento de la programación o caracteristica que nos permite segmentar el código por 
            funcionalidades o proposito.
            
        2. Crear una función para realizar la suma de los números impares en el rango de 0 a 100, 
            dentro de la función imprima los valores sumados y al final retorne el resultado de la sumatoria.
    """
    odds_list = list() # Odds numbers are those numbers whose cannot be divided by 2 parts or in other word are those whose number MODULE % of 2 is zero.
    
    for num in range(1, 100 + 1):
        if num % 2 != 0:
            odds_list.append(num)

    print("List of odds numbers found: ", odds_list)
    print("Its sum is: ", sum(odds_list))

#main_01()

def main_02():
    """
    ### Actividad: Diseñe una función para codificar strings y otra para decodificar strings.
    ---
    1. Revise documentación relacionada a los procesos de encriptación, explique brevemente como funcionan.
        Respuesta: Según observamos en clase Python nos ofrece ciertas útilidades para trabajar con la tabla de referencia ASCI 
        la cual hace referencia a los caracteres en formato numerico.
    2. Ambas funciones deben tener como entrada un string y una ¨Clave", la ¨Clave¨ será usada para codificar y decodificar.
    3. El desarrollo de está actividad esta abierto a multiples soluciones, por favor sea original en su respuesta.
    """
    def codifier( val : str, clave: str ):
        print("Coded value: ")
        coded_val =  f"{clave}-"
        
        for char in val:
            coded_val +=  f"*{ord(char)}" 
        else: 
            coded_val = coded_val + f"-{clave}"
            
        print(coded_val)    
        return coded_val 
       
    def decodifier(val : str, clave: str):
        print("\nThe resulted value is...")
        
        coded_value = val.split(f"-")[1]
        result = ""
                        
        for char in coded_value.split("*"):
            if char != '':
                result += chr( int(char) )
        
        print(result)
                
    valor = input("Valor a codificar:")
    get_value = codifier(valor, "^^^")
    
    decodifier(get_value,"^^^")
    
#main_02()


import os
import random

def main_03():
    """
    ### Actividad: Diseñe y codifique una función.

    1. Diseñe una función que revise el contenido de una carpeta, la mision de esta funcion es revisar todas las carpetas existentes y 
    obtener los nommbres de los archivos contenidos.
    2. Considere que dentro de cada carpete pueden existir otras carpetas.
    3. Todas las carpetas deben ser revisadas.
    4. Con la ejecucion de la siguiente celda se crearan las carpetas y los archivos.
    5. Es posible que debas considerar el uso de una función recursiva.
    """
    global numeracion_del_archivo, numero_de_sub_carpetas, max_carpetas
    
    max_carpetas = 4
    numeracion_del_archivo = 0
    numero_de_sub_carpetas = 0
    ruta_actual = os.path.join(os.path.abspath("./"), "Carpeta_principal")

    def guardar_archivo(text_content, file_path):
        with open(file_path, 'w') as file:
            # Write the text content to the file
            file.write(text_content)

    # Inicialización
    if os.path.exists("Carpeta_principal"):
        os.system(f'rmdir -r "Carpeta_principal"')
        os.mkdir("Carpeta_principal")
    
    def crear_carpetas(ruta_actual):
        global numeracion_del_archivo, numero_de_sub_carpetas
        numero_de_archivos_o_carpetas = random.randint(0,15) # genración de numero aleatorio entre 0 y 15.
        
        print(ruta_actual)
        
        if numero_de_sub_carpetas < max_carpetas:
            for n in range(0, numero_de_archivos_o_carpetas):
                numero_aleatorio_2 = random.randint(0,2) # número aleatoria entre 0 y 1.
                if numero_aleatorio_2 == 0:
                    os.mkdir(ruta_actual +'/'+ 'folder_{}'.format(n) )
                    print(ruta_actual +'/'+ 'folder_{}'.format(n))
                else:
                    contenido_del_archivo = "Contenido_{}".format(numeracion_del_archivo)                
                    ruta_del_archivo = ruta_actual + '/' + "archivo_{}.txt".format(numeracion_del_archivo)
                    guardar_archivo(contenido_del_archivo, ruta_del_archivo)
                    numeracion_del_archivo += 1
                    
            lista_de_nuevas_carpetas = [f.path for f in os.scandir(ruta_actual) if f.is_dir()] # Busqueda de nueva carpeta

            numero_de_sub_carpetas += 1
            for carpeta in lista_de_nuevas_carpetas:
                crear_carpetas(carpeta)
            
    #init
    crear_carpetas(ruta_actual)

#main_03()

import json

def main_04():
    """
    #### Actividad: Crear diccionarios y guardarlos como archivo JSON.
    De la unidad 11 sección 4.6 revise el ejemplo mostrado.
    Genera un diccionario, sobre la información que deseas guardar como base de datos, desarrollo el código necesario para generar el 
    archivo JSON, y también el código para cargar la información del archivo JSON.
    """
    
    option = input("""Menu:
     (1) Write information
     (2) Read Information      
    """)
    
    if int(option) == 1 and option.isdigit():
        data = []
        
        try:
            with open('data.json',"r") as file:
                data = list( json.load(file) )
        except:            
            data = []
            
        with open('data.json', "tw+") as file:
            
            print(data)

            title = input("Introduce the title: ")
            description = input("Introduce the description: ")

            data.append({ "title": title, "description": description })
                        
            json.dump(data, file) 
            
    elif int(option) == 2 and option.isdigit():
         with open('data.json',"r") as file:
            data = json.load(file)
            print(data)
    else:
        print("La opcion seleccionada no exist vuelva a intentarlo.")
    
#main_04()

def main_05():
    """
    #### Actividad: Uso de la funcion Lambda.
    ##### Instrucciones

    1. Escriba una función regular donde se realice una operación.
    2. Escriba la misma función donde use la expresión lambda.
    3. Explica brevemente las ventajas de usar la función Lambda.
    """
    
    def func01(x):
        return x ** 2
        
    func01(2)
    
    func02 = lambda x: x **2
    func02(2)
    
    # Ventaja de las Lambdas, su simplicidad para expresar cosas simples y manteniendo el codigo simple...
    
def main_06():
    """
    ### Actividad: Usar la función map para duplicar el valor de cada uno de los elementos contenidos.
    #### Instrucciones:

    """
    #1. Describa brevemente el funcionamiento y las ventajas de usar la función map
    # La simplicidad de lograr una proyeccion con esta misma es impresionante, tambien mencionar que la misma ofrece una version sencilla o minimalista.
    
    #2. Escriba el código en el siguiente espacio.
    my_numbs = [2, 4, 6, 8, 10]
    
    print( list( map(lambda x: x**2, my_numbs )) )
    
    
main_06()