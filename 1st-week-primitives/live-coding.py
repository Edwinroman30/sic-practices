# Edwin Roman, Rep. Dominicana Lun a Mier

opt = 1

print("Bienvenid@s a nuestro sistema:")

def calcular_descuento(total : float, porcentaje : float):
    return total * porcentaje

while opt != 0:
    opt = int(input("¿Que opcion deseas? \n (1). Comprar \t (2). Salir\n"))
    porcentaje = 0
    
    if opt == 1:
        print('OFERTAS\nPor compras mayores a $100 tienes un descuento de %5 en $')
        print('Por compras mayores a $200 tienes un descuento de %10 en $ \n')
        total = float(input("¿De cuanto es su compra?\n"))
        
        if (100 < total) and (total < 200):
            porcentaje = 0.05
            total = calcular_descuento(total, porcentaje)
        else:
            if total > 200:
                porcentaje = 0.10
                total = calcular_descuento(total, porcentaje)
        print("El total de su compra es: ", total)
        
        if porcentaje != 0:
            print("Por su compra obtuvo un descuento de:", porcentaje * 100, "%")
            
    elif opt == 2:
        opt = 0
        break
    else:
        print("La opcion proporcionada no existe :/")
        break
        
print("Gracias por elegirnos, vuelva pronto!")

