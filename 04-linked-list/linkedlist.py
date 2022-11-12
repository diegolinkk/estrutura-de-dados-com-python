from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self,elem):
        if self.head:
            pointer = self.head
            #começa na cabeça e enquanto próximo não for None
            #quando a expressão for falsa, o while sai e o pointer estará no lugar que queremos
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1


    #método especial do Python que permite usar o len(elemento)
    def __len__(self):
        return self._size
    

    #se a linguagem não oferece sobrecarga de operador, eu implantaria nesses métodos
    def get(self,index):
        # a = lista.get(1)
        pass

    def set(self,index,elem):
        #lista.set(5,1)
        pass
    
    #método especial do Python que permite usar o [] como uma lista
    def __getitem__(self,index):
        #a = lista[6]
        #esse método é conhecido de "sobrecarga de operador"
        """Aqui ele vai percorer x vezes elementos dentro de um laço e caso esse elemento existir, retorna um dado, caso contrário, retorna um erro"""

        pointer = self.head
        for i in range(index):
            #se o pointer não for None, posso avançar
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        
        if pointer:
            #se houver o elemento, retorna o valor
            return pointer.data

        raise IndexError("list index out of range")


    #método especial do Python que permite usar o 
    def __setitem__(self,index,elem):
        #lista[5] = 15

        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        
        if pointer:
            #diferente da função anterior, aqui teve que colocar um else, pq ele não retorna um valor, então acaba executando a linha seguinte
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
    
    def index(self, elem):
        """Retorna o índice do elemento na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in list".format(elem))


