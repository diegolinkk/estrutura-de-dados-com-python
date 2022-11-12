def busca(lista,elemento):
    """Busca elemento na lista e caso encontrar,retorna índice,caso contrário retorna None  """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
        
    return None


lista = ['cachorro','gato',1,3,32]
elemento = 'gato'
indice = busca(lista,elemento)

if indice is not None:
    print("O elemento {} foi encontrado no índice {}".format(elemento,indice))
else:
    print("Elemento não encontrado")