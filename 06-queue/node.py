class Node:
    """armazena o dado propriamente dito e o dado do nó seguinte"""
    def __init__(self,data):
        self.data = data
        self.next = None

# # exemplo de uso
# no1 = Node(5)
# no2 = Node(10)

# print(no1.data)
# print(no2.data)

# #amarrando o nó 1 no nó 2
# no1.next = no2

# #exibindo o dado do nó seguinte ao 1
# no1.next.data
# print(no1.next) #exibe o endereço de memória