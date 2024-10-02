from pilha import Pilha

p = Pilha()

def maiorNum(self):
    maior = self[0]
    guardar = []
    while not p.is_empty():
        guardar.append(p.top())
        verificar = p.pop()
        if verificar > maior:
            maior = verificar
        
    for c in range(len(guardar), 0, -1):
        p.push(guardar[c-1])

    return maior



p.push(5)
p.push(3)
p.push(9)
p.push(2)
maior = maiorNum(p.pilha)
print(maior)