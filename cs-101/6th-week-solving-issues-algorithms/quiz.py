def main01():
    ''' 
    Quiz
    Q1.
    En el problema del intercambio de monedas, supongamos que hay una moneda de 400 wones.
    Si es así, escriba el resultado de cómo el algoritmo coin_change() determinará el cambio de la moneda de 800 wones.
    '''
    # A naive version.
    def changec_coin_greedy_approach(amount: int, coins: list):
        # Selectation of the entry/input.
        highter_amount_index = 0
        finals_coins = []
        
        # Checking the it's correctness or the probability it has to satisfy the problem.
        while amount > 0:
            if coins[highter_amount_index] > amount:
                highter_amount_index += 1
            else:
                finals_coins.append( coins[highter_amount_index] )
                amount -= coins[highter_amount_index]
        
        # Verify if the given inputs, satisfy the problem. (When)
        return finals_coins

    print("Result : ", changec_coin_greedy_approach(800, coins = [500, 400, 100, 50, 10]) )
    ## Respuesta: [500, 100, 100, 100]

def main02():
    ''' 
    Q 31-01 - Tienes 8 monedas idénticas numeradas del 1 al 8. De estas, solo una moneda es más pesada que la otra.
    Suponiendo que puede pesar monedas con una balanza equilibrada, diseñe un algoritmo que encuentre la moneda más pesada.
    En este momento, ¿cuántas veces se debe usar al menos la balanza? 
    '''
    coins = [1,2,3,4,5,6,7,8,9]
    weighest = coins[0]
    counter = 0
    
    for x in range(1, len(coins)):
        
        counter += 1
        if coins[x] >= weighest:
            weighest = coins[x]
    print("Moneda de mayor peso: ", weighest)
    print("Las básculas comparativas se utilizaron: ", counter, " veces.")
    return weighest

#main02()

def main03():
    
    from math import sqrt, floor # Importación de ciertas librerías especializadas de matemática para calcular raiz cuadrada y redondear.
    import time # Para fines de estimación del tiempo.


    def is_square_digitsum(n): # Utilizado para evaluar si el valor proporcionado es cuadratico, retorna si True si lo es, contrario False. 
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        if sqrt(s) == int(sqrt(s)):
            return True
        return False


    def find_all_squares(): # Retorna una lista de longitud de 5 elementos, de los cuadrados base 10, para ser utilizados en el remplazado de palabras.
        sqrs = [[] for _ in range(5)]
        for i in range(1, floor (sqrt(10 ** 5)) + 1):
            n = i * i
            if not is_square_digitsum(n): # Utiliza la funcion anterioremente comentada, cuya tarea es determinar si el valor proporcionado verdaderamente es cuadratico.
                continue
            s = str(n)
            if len(s) == 3 and s[1] != s[2]:
                continue
            if len(s) == 5 and s[2] != s[3]:
                continue
            if len(s) in [4, 5] and len(set(s)) != 4:
                continue
            sqrs[len(s) - 1].append(n)
        return sqrs # Lista de elementos cuadraticos.


    def promising (s, n, dic):
        for i in range(len(s)):
            digit = int(str(n)[i])
            for key, value in dic.items():
                if key == s[i] and value != digit:
                    return False
                if value == digit and key != s[i]:
                    return False
        return True


    def solve(words, dic, squares): # Su responsabilidad es asociar o establecer relación entre las palabras y los valores cuadraticos asignando estos mismos en un diccionario.
        global solved 
        if (len(words) == 0):
            solved = dic
        else:
            s = words[0]
            candidates = squares[len(s) - 1]
            for n in candidates:
                if promising(s, n, dic):
                    newdic = dic.copy()
                    for i in range(len(s)):
                        newdic[s[i]] = int(str(n)[i])
                    solve(words [1:], newdic, squares)

            
    def main():
        squares = find_all_squares()
        # print(squares)
        words = ['A', 'TO', 'ALL', 'XMAS', 'MERRY']
        dic = {}
        solve (words, dic, squares) # Como mencionada anteriormente, su trabajo es asociar o establecer relación entre las palabras y los valores cuadraticos asignando estos mismos en un diccionario.
        for word in words:
            print (word, end=": ")
            for c in word:
                print(solved[c], end="")
            print()

    start = time.time() #Tiempo iniciar de ejecución
    solved = {}
    main() # Ejecución de las funciones asociadas, que permiten el resultado final.
    end = time.time() #Tiempo de finalización de la ejecución
    print("Elapsed Time:", end-start,"seconds") # Tiempo neto.