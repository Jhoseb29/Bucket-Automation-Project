from dataclasses import dataclass

@dataclass
class Stack:

    __items = []

    def items(self):
        return self.__items

    def push(self, item):       
        self.__items.append(item)
    
    def top(self):
        return self.__items[-1]
    
    def pop(self):
        return self.__items.pop()
    
    def bottom(self):
        return self.__items[0]

    def is_empty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)
    
    def sorted_insert(self, key):
        
        if not self.__items or key.size > self.__items[-1].size:
            self.__items.append(key)
            return
        
        top = self.__items.pop()

        self.sorted_insert(key)
        self.__items.append(top)

    def sort_stack(self):

        if not self.__items:
            return
        
        top = self.__items.pop()
        self.sort_stack()
        self.sorted_insert(top)
