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
