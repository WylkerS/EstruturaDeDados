class PilhaVazia(Exception):
    pass

class Pilha:

    def __init__(self):
        self.pilha = []

    def __len__(self):
        return len(self.pilha)
    
    def push(self, num):
        self.pilha.append(num)

    def is_empty(self):
        return len(self.pilha) == 0
    
    def pop(self):
        if self.is_empty():
            raise PilhaVazia("A pilha está vazia")
        return self.pilha.pop()
    
    def top(self):
        if self.is_empty():
            raise PilhaVazia("A pilha está vazia")
        return self.pilha[-1]
    
