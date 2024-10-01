from pilha import Pilha

p = Pilha()

def inverte(lista):
    for c in lista:
        p.push(c)

    lista.clear()
    
    while not p.is_empty():
        lista.append(p.pop())
    


numeros = [0, 1, 2, 4]
inverte(numeros)

print(p.pilha)
print(numeros)