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

''' Merge function into the merge sort algoritm for two ordered linkedList.'''
def merge_sort_recursive(node_a : Node, node_b : Node):
    # Base cases:
    if node_a == None: 
       return node_b # If the "node_a" linkedList is empty, that's mean the more higher elements rest in node_b.
    if node_b == None: 
       return node_a # If the "node_b" linkedList is empty, that's mean the more higher elements rest in node_a.
    
    if node_a.val < node_b.val:
        node_a._next = merge_sort_recursive(node_a._next, node_b)
        return node_a
    else:
        node_b._next = merge_sort_recursive(node_a, node_b._next)
        return node_b
        

def main():
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    
    # List A
    n2.set_next(n3)
    n3.set_next(n4)
    
    # List B
    n1 = Node(1)
    n5 = Node(5)
    
    n1.set_next(n5)
    
    sortedList = merge_sort_recursive(n1, n2)    
    print(sortedList)

main()