lista = [1,2,3,4,5,6]

def inverter(lista):
    nova_lista = []
    for i in range(len(lista) -1,-1,-1):
        nova_lista.append(lista[i])
    
    return nova_lista


lista_invertida = inverter(lista)
print(lista_invertida)