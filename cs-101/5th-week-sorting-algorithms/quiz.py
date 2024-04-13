''' 
 ¿Cuántas comparaciones se ejecutaron en el siguiente proceso de ordenamiento de burbuja?
'''
def bubbleSort(S):
    n = len(S)
    counter = 0
    
    for i in range(n):
        print(S)
        for j in range(n-1):
            counter += 1
            if S[j] > S[j+1]:
               S[j] , S[j+1] = S[j+1] , S[j]
    
    print("Comparision: ", counter)
    
S = [50, 30, 40, 10, 20]
#bubbleSort(S)

def insertionSort2(S):
    n = len(S)
    counter = 0

    for i in range(1,n):
        print(S)
        x = S[i]
        j = i - 1

        while j >= 0 and S[j] > x:
            counter += 1
            S[j+1] = S[j]
            j -= 1
        S[j + 1] = x
    print("Comparision result: ", counter)

#insertionSort2(S)

def merge2(S, low, mid, high):
    R = []
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if S[i] < S[j]:
            R.append(S[i]); i += 1
        else:
            R.append(S[j]); j += 1
    if i > mid:
        for k in range(j, high + 1):
            R.append(S[j])
    else:
        for k in range(i, mid + 1):
            R.append(S[i])
    for k in range(len(R)):
        S[low + k] = R[k]

def ordenamiento_fusion2(S: list, low, high):
    count = 0
    print("UNO")
    if low < high:
        print(S)
        mid = (low + high) // 2
        ordenamiento_fusion2(S, low, mid)
        ordenamiento_fusion2(S, mid + 1, high)
        merge2(S, low, mid,+ high)
        return count + 1
    
print("Times executed: ", ordenamiento_fusion2(S, 0, len(S) - 1) )

''' 
Buenas noches maestra, por esta vía procedo a analizar los tres algoritmo de ordenamiento visto en clase.
Bubble Sort = O(n*2)
Select Sort = O(n*2)
Insertion Sort = O(n*2)
Mi analisis esta fundamentado en la cantidad de bucles por entradas. Muchas gracias.
'''