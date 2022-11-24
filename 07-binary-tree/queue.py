class Node:
    """armazena o dado propriamente dito e o dado do nó seguinte"""
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node
        
        self._size = self._size + 1

    def pop(self):
        if self.first is not None:
            elem = self.first.data
            self.first = self.first.next
            self._size = self._size - 1
            return elem

        return IndexError("The queue is  empty")

    def peek(self):
        if self.first is not None:
            elem = self.first.data
            return elem

        return IndexError("The queue is  empty")

    def __len__(self):
        return self._size
    
    def __repr__(self):
        if len(self) > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "The Queue is empty"

    
    def __str__(self):
        return self.__repr__()