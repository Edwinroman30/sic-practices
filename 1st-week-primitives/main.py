"""
### **Actividad: Uso de operadores**

En esta actividad, usaras los operadores

#### **Instrucciones:**

1. Generar un loop que revise cada uno de los elementos contenidos en la lista llamada "lista_de_elementos".
2. Revisar el tipo de elemento.
3. Comparar si el valor esta por debajo del umbral definido, en ese caso imprimir la palabra ¨aprobado¨ en caso contrario imprimir ¨Rechazado¨
4. En el código incluya dos contadores, para contabilizar el número de aprobados y rechazados, al final del codigo imprima el total de cada uno de ellos.
5. Contabilize los elementos que son tipo string y de igual forma imprima final del loop el resultado.

"""
umbral = - 10
lista_de_elementos = [10, 3.14, "7", -5, "2.718", 42, "Python", -8.9, "Hola", 100.5, "Mundo", -15, "GPT-3", 5.5, "AI", -20, "2023", 123, "OpenAI", -2.5, "Ejemplo"]
conteo_strings = 0
aprobados = 0
rechazados = 0

def main():
    global rechazados, conteo_strings, aprobados
    for elem in lista_de_elementos:
        if( (type(elem) == int or type(elem) == float) and elem < umbral):
            print("Aprobado", elem)
            aprobados += 1
        elif(type(elem) == str):
            conteo_strings += 1
        else:
            print("NO aprobado", elem)
            rechazados += 1

    print("\nTotal aprobados: ", aprobados)
    print("Total rechazados: , ", rechazados)
    print("Total de strings: ", conteo_strings)

#Program Execution....
main()