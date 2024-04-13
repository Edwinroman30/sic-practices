# Sum numbers recursively.... from 1 to n.
# (1) Base case n = 1, return 1
# (2) Visual Sample
"""
n = 3; func(3) = 6

 3 +(3-1) = 6
[2]+(2-1)= 3
[1] = 1

"""
# (3) Generalize the pattern
# n + func(n - 1)

def sumar(n):
    #base condition
    if n == 1:
        return 1
    return n + sumar(n - 1)

#print(sumar(6))

#Factorial:
#Difficulty: Beginner
#Problem: Calculate the factorial of a non-negative integer n (n!).
# Base case If n <= 0 ->  1
# Human sample interpretation:
"""
n=3
3*2*1 = 6
n=4
4*3*2*1 = 24 
4*!3 = 24
"""
# Compute sample interpretation:
"""
func(3)
3 * func(3-1) => 6 
2 * func(2-1) => 2
1 * func(1-1) => 1
0 => 1

PATTERN:
n * func(n - 1)
"""
def factorial(n : int):
    #base condition
    if n <= 0:
        return 1
    return n * factorial(n - 1)

#print(factorial(3))


#EXERCISE 3
#Fibonacci Sequence:
#Difficulty: Beginner
#Problem: Calculate the nth Fibonacci number (0, 1, 2, 3, 5, ...).

# Base condition
# if n <= 0 RETURN 0 || n == 1 RETURN 1

# Set/find a pattern, from the base condition using simple use cases.
# func(n - 2) + func(n - 1)

# Understanding the problem as human and as computer
''' 
The 6th Fibonacci number is 8
n = 6
0, 1, 1, 2, 3, 5: 8

n = 4
0, 1, 1, 2: 3
    func(n - 2) + func(n - 1)
    func(4-2) + func(4-1)
    func(2) + func(3)
    [func(0)+func(1)] + [func(1)+func(2)] = [0+1] + [1 + [1]]
    1 + (2) = 3
    
n = 3
0, 1, 1: 2
    func(n - 2) + func(n - 1)
    func(3 - 2) + func(3 - 1)  
    func(1) + func(2)  =  1 + (func(2 - 2) + func(2 - 1)) 
    1 + (0 + 1) = 2
    
n = 2
0, 1: 1
    func(n - 1) + 1 = 1 + 1 = 2 (NO)
    func(n - 2) + func(n - 1)
    func(0) + func(1) = (0,1)
n = 1
0,1: 1

n = 0
0 = 0
'''

def fibonnaciSequence(nthFibonnaci):
    
    # Base condition
    if nthFibonnaci <= 0:
        return 0
    if nthFibonnaci  == 1:
        return 1
    
    return fibonnaciSequence(nthFibonnaci - 2) + fibonnaciSequence(nthFibonnaci - 1)

#print(fibonnaciSequence(6))

''' 
Binary Search:

Difficulty: Intermediate
Problem: Efficiently search for a target element in a sorted array.
Base case: If the search space is empty or the target is found, return the appropriate result.
Recursive case: Divide the search space in half based on the middle element, and recursively search the appropriate sub-array for the target. '''

# Base case
# if len(array) == 0: return []
# if len(array) == 1 and target in array: [target]

# if len(array) == 2 and target in array: return [target] (Deprecated)

# Human digestable sample / # Understanding the problem as human and as computer
''' 
target = 1
[2, 1, 3] 
=> sorted([1,2,3])
2 > 1
[1,2]
2>1
1

target 2
[1,2,3,4]
3 > 2
[1,2]
3 < 2
[]

target 4
[1,2,3,4]
3 > 4
[3,4]
3 < 4
[1,2,3]
'''

# Computer sample
''' 
target = 2
[2, 1, 3] => sorted([1,2,3])
if len([1,2,3])//2 >= target
    [1,2,3][0:len(array) + 1]
if len([1,2,3])//2 <= target
    
'''

# Find a pattern
# func(target, list)

def binary_s(array, target):
    #Base condition
    if len(array) == 0:
        return []
    
    middler_inx = len(array)//2
    
    #Patterns
    if array[middler_inx] > target:
        return binary_s(array[0: middler_inx], target)
    elif array[middler_inx] < target:
        return binary_s(array[middler_inx::], target)
    elif array[middler_inx] == target:
        return [target]
    else:
        raise Exception("NO se que pasa....")
    

print("Found element:", binary_s(sorted([1,2,3,4,32,3,5,7,6]), 4))

class Node:
    def __init__(self, val : int):
        self.val = val
        self._next = None
    
    def set_next(self, node):
        self._next = node
    
    def set_value(self, val : int):
        self.val = val

    def get_next(self):
        return self._next
    
    def __repr__(self):
        return str(self.val)

def reversing_linkedlist(node : Node):
    if node._next == None or node == None:
        return node
    
    lastNode = reversing_linkedlist(node._next)
    
    node.get_next().set_next(node)
    node.set_next(None)    
    return lastNode

def main_01_reversing_linkedlist():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    
    n1.set_next(n2)
    n2.set_next(n3)
    n3.set_next(n4)
    n4.set_next(n5)
        
    lastnode = reversing_linkedlist(n1)    
    print(lastnode)

def atm_with_recursion():
    
    papeletas = [100,200,500,1000]
    option_bank = 0

    def Proceso(monto):
        for papeleta in papeletas:
            #print(monto//b)
            if(monto/papeleta == 1):
                print('Se le ha dado 1 billete de {}'.format(papeleta))
                exit()

            if((monto//papeleta) != 0):
                devueltas.append([monto//papeleta,papeleta])
        
        devueltas_finales = sorted(devueltas)
        #Con esto se puede lograr pagar con las papeletas mayores, lo cual  puedo dar las de mayor valor que seria menos
        #fisicamente que es lo que se logra o persive buscar. (LOGICO MUCHO, FISICO POCO.)

        #print(devueltas_finales)

        for dev in devueltas_finales:
            print('Se le ha dado ',dev[0],' billetes de ',dev[1])
            monto = monto - (dev[0]*dev[1])
            #break (Para comprobar el monto o la valides de la operacion)
            if(monto >= 100):
                Proceso(monto)
            else:
                exit()

        print('MOnto total: {}'.format(monto))
        #FIN FUNCION

    print('Cajero  Automatico.net')

    monto_cuenta = int(input('Ingrese su monto a retirar: '))

    print('(1) FDP Inversments(Bank) \n(2) Any Bank')
    option_bank = int(input())


    if(monto_cuenta == 0 or monto_cuenta < 100):
        print('Sea conciente, debe retirar 100 pesos en adelante.')
        exit()

    if(option_bank == 1):
        if(monto_cuenta > 20000):
            print('Lo sentimos usted no puede solicitar mas de 20000 pesos.')
        else:
            devueltas = []
        Proceso(monto_cuenta)
    else:
        if(monto_cuenta > 10000):
            print('Lo sentimos usted no puede solicitar mas de 10000 pesos.')
            print('El otro banco para la próxima, esta en desarrollo. (COMING SOON)')