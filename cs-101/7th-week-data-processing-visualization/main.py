''' 
    # Actividad: Importación de módulos y su uso.
    ## Instrucciones


#1. Importe los módulos que te permitan trabajar con fechas y tiempo (modulo datetime).
import datetime

#2. Use los diferentes métodos relacinados a operaciones con fechas y hora. (Interactuando con los metodos)

fecha_hoy = datetime.date.today()
fecha_futura = datetime.date(2024, 12, 31)

diferencia = fecha_futura - fecha_hoy
print("Diferencia entre fechas: ", diferencia)

fecha_actual = datetime.datetime.now()
print("Fecha today: ",fecha_actual)  # Salida: 2024-3-7 12:34:56.789123
print("Fecha now: ", datetime.datetime.today())

fecha_formateada = fecha_hoy.strftime("%d/%m/%Y")
print("Fecha preformateada: ", fecha_formateada)  # Salida: 7/3/2024

print("\n Datos del ejercicios: \n")

#3. En el siguiente apartado revisa cada una las fechas contenidas en la lista e imprima el número de semanas y los dias 
# restantes para llegar a esa fecha. 
# Espacio disponible para desarrollar el código y agregar los comentarios necesarios.

lista_de_fechas = ['04/01/2024', '01/28/2024', '03/16/2024', '05/24/2024', '07/30/2025']
current_date = datetime.datetime.now()

for date in lista_de_fechas:
    date_representation = datetime.datetime.strptime(date,"%m/%d/%Y")
    resting_days = date_representation - current_date
    resting_weeks = resting_days.days // 7
    
    print("Para la fecha: ", date_representation)
    print("Restan ",resting_days.days, " dias.")

    print("Semanas: ", resting_weeks)
    
    print("Resume...", datetime.timedelta(days= resting_days.days, seconds=resting_days.seconds))
    print("")
'''

''' 
# Actividad: Manejo de la biblioteca Pandas.

## Instrucciones
1. Crear una serie de pandas, donde su indice este compuesto por fechas y en columna principal almace los valoras cargados en una lista.
2. Graficar los valores de la lista en función de la fecha.
'''
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Espacio para desarrollar el código y agregar los comentarios necesarios.
def main():
    precios = [140, 130, 120, 115, 160, 110, 170, 150, 157, 135]

    my_serie = pd.Series(precios)
    end_date = datetime.datetime.today() + datetime.timedelta(days= len(precios))
    
    my_serie.index = pd.date_range(datetime.datetime.today(), end_date.date())
    #[ (datetime.datetime.now() + datetime.timedelta(days= x)) for x in range(1, len(precios) + 1)]

    print(my_serie.shape)

    ''' Arreglarlo, mirar las laminas de samsung y ver como se hace. '''
    graph = my_serie.plot.bar(x=my_serie.index.names, y=my_serie.iloc[0])
    graph.set_xlabel("Fechas")
    graph.set_ylabel("Cantidades")

    plt.show()


''' S = ["element 1", "element 2", "element 3", "element 4", "element 5", "element 6", "element 7", "element 8"]
Sr = pd.Series(S)
Sr.index = ['a', 'b','c','d','e','f','g','h']

print(Sr['c'])
print("\n")
print(Sr[ ['e', 'f'] ])
 '''

def main_02():
    ''' 
    ## Instrucciones
      1. Dado el siguiente diccionario construya un objeto DataFrame.
      2. Filtre los resultados por año de publicación.
      3. Obtenga algunas columnas basado en que contenga alguna palabra en el nombre de la publicacion.    
    '''
    publicaciones_literarias = {
        1605: "Don Quijote de la Mancha - Miguel de Cervantes",
        1865: "Alicia en el país de las maravillas - Lewis Carroll",
        1949: "1984 - George Orwell",
        1954: "El Señor de los Anillos - J.R.R. Tolkien",
        1997: "Harry Potter y la piedra filosofal - J.K. Rowling",
        2003: "El Código Da Vinci - Dan Brown"
    }

    # Espacio para desarrollar el código y agregar los comentarios necesarios.
    my_dataframe = pd.DataFrame.from_dict({ "Release Year" : publicaciones_literarias.keys(), "Book Title" : publicaciones_literarias.values() })
    
    print("2. Filtre los resultados por año de publicación: ")
    print(my_dataframe["Release Year"])

    print("\n3. Obtenga algunas columnas basado en que contenga alguna palabra en el nombre de la publicacion.")
    print(my_dataframe.loc[ my_dataframe["Book Title"].str.contains("El") ])
    
main_02()

def main_03():
    ''' Actividad: Operaciones con DataFrames.

        ## Instrucciones
        1. Descargue el archivo ted.csv del siguiente link: https://www.kaggle.com/datasets/rounakbanik/ted-talks
        y guardelo en el mismo directorio donde está localizado el notebook.
    '''

    print("# 2. Lea el archivo csv como un dataframe.", "\n")
    ted_data = pd.read_csv("./resources/ted_main.csv")
    
    print("#3. Muestre la cabecera o las primeras files del DataFrame.", "\n")   
    print(ted_data.head(10), "\n")
    
    print("#4. Verifique el tipo de datos contenido en cada una las columnas.", "\n")
    print( ted_data.info(), "\n" )
    
    print("#5. Verifique el número de registros perdidos.")
    print(ted_data[ted_data.isnull() | ted_data.isna()].count(), "\n")
    
    print("#6. En una columna adicional calcule el número de comentarios entre el número de vistas.")
    comments = ted_data["comments"].sum()
    views = ted_data["views"].sum()
    
    print("Sum of views: ", views)
    print("Sum of comments: ", comments)
    result = comments / views
    
    print("Resultado obtenido:", result)
    
        
#main_03()