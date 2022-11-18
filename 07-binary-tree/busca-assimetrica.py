from tree import BinaryTree,Node


tree = BinaryTree()

n1 = Node('I')
n2 = Node('N')
n3 = Node('S')
n4 = Node('C')
n5 = Node('R')
n6 = Node('E')
n7 = Node('V')
n8 = Node('A')
n9 = Node('5')
n10 = Node('3')
n11 = Node('-')

tree.root = n10
n10.left = n6
n10.right = n9

#lado esquerdo
n6.left = n1
n6.right = n5
n5.left = n2
n5.right = n4
n4.right = n3

#lado direito
n9.left = n8
n8.right = n7

#incluindo o hífen do -se
n9.right = n11

tree.postorder_traversal() 
print("Altura: {}".format(tree.height()))

#também é possível mudar a raiz para calcular a altura de uma sub-árvore
tree.root = n5
print("Altura do nó R: {}".format(tree.height()))