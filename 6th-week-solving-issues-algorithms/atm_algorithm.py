# Edwin ROman
''' 
¿Qué sucede si la cantidad de monedas para el cambio es limitada?
 Ejem: Se tiene almacenado para el cambio la siguiente cantidad; 1 de 500w, 1 de 100w,
        3 de 50w y 2 de 10w.
    - ¿ Cómo se debe distribuir 710 para el cambio ?
'''
monedas = [(1,500),(1,100),(3,50),(2,10)]
cant = 710 #int(input("Introduzca monto: ")) # 710
selected_coins = []

def cambio_moneda2(coins, amount):
    global selected_coins
    possibles_coins = [] # What client expect.
    
    lowest_coin = min(map(lambda x : x[1] , coins))

    # Base case of recurtion
    if amount < lowest_coin:
        return   
    
    # (1) Selectation of the entry/input.
    for coin_quatity, coin_value in coins:
        possible_divisions = (amount // coin_value)
        
        # (2) Checking the it's correctness or the probability it has to satisfy the problem.
        if possible_divisions != 0:
            
            for quantity in range(coin_quatity, 0, -1): # Checking if amount can be divided from the most higher quantity of coin value.
                if (quantity * coin_value) <= amount:
                    possibles_coins.append( [quantity, coin_value] )
                    break
        
    # (3) Verify if the given inputs, satisfy the problem. (When)
    possibles_coins = sorted(possibles_coins)
    possibles_coins = sorted(possibles_coins, key= lambda x: x[1], reverse= True)

    choosen_coin = tuple(possibles_coins[0]) # The most higher divisor, from the list.
    
    selected_coins.append( choosen_coin  )
    amount -= choosen_coin[0] * choosen_coin[1]
    
    #Updating the coin values
    coins = list( map(lambda x: x if x[1] != choosen_coin[1] else (x[0]-choosen_coin[0], choosen_coin[1]), coins) )
        
    return cambio_moneda2(coins, amount)    
      
cambio_moneda2(monedas, cant) ### Desarrollar función
print("Para una cantidad a retirar de: ", cant)
print("Lista de billetes a retornar: ", selected_coins)