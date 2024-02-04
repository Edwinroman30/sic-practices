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