#construa um algorítmo que verifica se tem itens duplicados

def duplicado(lista):
    for i in range(0,len(lista) -1):
        for j in range(i + 1,len(lista)):
            if lista[i] == lista[j]:
                print("tem duplicado")
                return True
    
    print("não tem duplicado")
    return False
    

duplicado("sal");