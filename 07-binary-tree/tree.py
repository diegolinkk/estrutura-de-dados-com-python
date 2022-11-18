class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self,data=None):

        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    #percurso em ordem simétrica (inorder em inglês)
    def simetric_traversal(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')',end='')
    
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)

        print(node.data)
    
    def height(self, node = None):
        """calcula a altura da árvore"""
        if node is None:
            node = self.root
        
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)

        if hright > hleft:
            return hright + 1
        return hleft + 1

        
#     #exemplo simples de implantação
#     tree = BinaryTree(7)
#     tree.root.left = Node(18)
#     tree.root.right = Node(14)
#     print(tree.root)
#     print(tree.root.right)
#     print(tree.root.left)