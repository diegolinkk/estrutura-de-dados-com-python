from tree import BinaryTree,Node

#implementação de busca simétrica
tree = BinaryTree()
n1 = Node('a')
n2 = Node('+')
n3 = Node('*')
n4 = Node('b')
n5 = Node('-')
n6 = Node('/')
n7 = Node('e')
n8 = Node('c')
n9 = Node('d')

tree.root = n2
n2.left = n1
n2.right = n3
n3.left = n4
n3.right = n5
n5.left = n6
n5.right = n7
n6.left = n8
n6.right = n9

tree.simetric_traversal()