def main():
    ''' 
    ## Q 22-01

    La siguiente es la implantación de una pila. ¿Cuál será el resultado del siguiente código?
    ```
    ```
    **Respuesta:**
    ['Banana', 'Apple', 'Strawberry']
    '''
    class Stack():
        def __init__(self) -> None:
            self.internal_stack = []
        
        def is_empty(self) -> bool:
            return True if len(self.internal_stack) == 0 else False
        
        def push(self, item: any):
            self.internal_stack.append(item)
            return item
        
        def pop(self):
            return None if self.is_empty() else self.internal_stack.pop()
    
    stack = Stack()
    stack.push("Banana")
    stack.push("Apple")
    stack.push("Tomato")
    stack.pop()
    stack.push("Strawberry")
    stack.push("Grapes")
    stack.pop()
    
    print(stack.internal_stack)
    
    
#main()

def main_02():
    """
    ## Q 22-02
    La siguiente es la implantación de una pila. ¿Cuál será el resultado del siguiente código?
    """
    class Stack():
        def __init__(self) -> None:
            self.internal_stack = []
        
        def is_empty(self) -> bool:
            return True if len(self.internal_stack) == 0 else False
        
        def push(self, item: any):
            self.internal_stack.append(item)
            return item
        
        def pop(self):
            return None if self.is_empty() else self.internal_stack.pop()
        
        def __str__(self):
            return str(self.internal_stack)
        
    stack = Stack()
    items = [10 * i for i in range(1,10)]
    for item in items:
        stack.push(item)
        if (item // 10) % 2 == 0:
            stack.pop()
    print(stack)
    
#main_02() 
# Retornara una lista de los impares desde el 10 al 90.

def main_03():
    ''' 
    ## Q 23-01
    La siguiente es la implantación de una pila. ¿Cuál será el resultado del siguiente código?
    '''
    
    class Queue():
        def __init__(self) -> None:
            self._queue = []

        def enqueue(self, item: any):
            self._queue.append(item)
            return item
        
        def dequeue(self):
            return None if self.is_empty() else self._queue.pop(0)
        
        def is_empty(self):
            return True if len(self._queue) == 0 else False
        
        def clear(self):
            self._queue.clear()
        
        def __repr__(self) -> str:
            return str(self._queue)
            
    queue = Queue()
    queue.enqueue("Banana")
    queue.enqueue("Apple")
    queue.enqueue("Tomato")
    queue.dequeue()
    queue.enqueue("Strawberry")
    queue.enqueue("Grapes")
    queue.dequeue()
    print(queue) 
    # ['Tomato', 'Strawberry', 'Grapes']
    
# main_03()

def main_04():
    ''' 
    ## Q 23-02

    La siguiente es la implantación de una cola. ¿Cuál será el resultado del siguiente código?

    **Respuesta:**
    '''
    class Queue():
        def __init__(self) -> None:
            self._queue = []

        def enqueue(self, item: any):
            self._queue.append(item)
            return item
        
        def dequeue(self):
            return None if self.is_empty() else self._queue.pop(0)
        
        def is_empty(self):
            return True if len(self._queue) == 0 else False
        
        def clear(self):
            self._queue.clear()
        
        def __repr__(self) -> str:
            return str(self._queue)
            
    
    queue = Queue()
    items = [10 * i for i in range(1,10)]
    for item in items:
        queue.enqueue(item)
        if (item // 10) % 2 == 0:
            queue.dequeue()
    print(queue)
    
#main_04() # [50, 60, 70, 80, 90]

def main_05():
    ''' 
    ## Q 24-01

    ¿Cuál es el algoritmo de la siguiente función `find_two()`?
    ```
    RESPUESTA: El mismo utiliza un algoritmo de busqueda de secuencia para determinar el valor minimo y maximo de valores dentro de un arreglo numerico.
    
    ```
    Analice el código y escriba el resultado de la ejecución.
    RESPUESTA: Como respuestas tenemos dos valores que representaran el valor minimo y maximo encontrado.
    '''
    def find_two(nums):
        x = y = 0
        counter = 0
        
        for i in range(1, len(nums)):
            if nums[x] < nums[i]:
                x = i
            elif nums[y] > nums[i]:
                y = i
                
            counter += 1
        print("How many step do we made to find the solution? ", counter)
        return x,y

    nums = [11, 37, 45, 26, 59, 28, 17, 53]
    i,j = find_two(nums)
    print(nums[i], nums[j])


main_05()


def main_06():
    ''' 
    El siguiente es el código para el juego de combinación de números.
    Si el máximo es 100 y el número es 51, ¿cuál es la salida de `count`?
    ``` '''
    maximo = int(input("Ingrese el número maximo: "))
    numero = int(input("Ingrese tu intento de adivinar el numero: "))
    low, high = 1, maximo
    count = 0
    while low < high:
        count += 1
        mid = (low + high) // 2
        if mid == numero:
            print(f"El número es {numero}")
            break
        elif mid > numero:
            high = mid - 1
        else:
            low  = mid + 1

    print(f"Total {count} veces fue buscado.")

#main_06()


def main_07():
    ''' 
      Usando la función hash de la clase HashTable, calcule la clave y la clave hash de "Alicia en el país de las maravillas"
      de la siguiente manera. (El valor clave es 1763.)
    '''
    class HashTable02():

        def __init__(self):
            self.MAX_INDEX = 20
            self.hashStorage = [ None for x in range(self.MAX_INDEX) ]
        
        def hast_function(self, key):
            pass
        
        def set_item():
            pass
        
        def get_item():
            pass
    
    class HashTable:
    
        def __init__(self, size):
            self.size = size
            self.table = {}
            for i in range(size):
                self.table[i] = []

        def hash(self, key):
            return key % self.size

        def put(self, key, value):
            bucket = self.table[self.hash(key)]
            if value not in bucket:
                bucket.append(value)

        def get(self, key):
            return self.table[self.hash(key)]
    
    table = HashTable(8)
    book  = "Alice in Wonderland"
    key = sum(map(ord, book))
    print(key, table.hash(key))

def main_08():
    
    class HashTable:
    
        def __init__(self, size):
            self.size = size
            self.table = {}
            for i in range(size):
                self.table[i] = []

        def hash(self, key):
            return key % self.size

        def put(self, key, value):
            bucket = self.table[self.hash(key)]
            if value not in bucket:
                bucket.append(value)

        def get(self, key):
            return self.table[self.hash(key)]
    
    table = HashTable(8)
    book  = "Alice in Wonderland"
    key = sum(map(ord, book))
    print(key, table.hash(key))
