from pilha import Pilha

p = Pilha()

def RemoverRecursivamente():
    if p.is_empty():
        return None
    p.pop()
    return RemoverRecursivamente()


p.push(5)
p.push(3)
p.push(3)
p.push(2)
RemoverRecursivamente()
print(p.pilha)
