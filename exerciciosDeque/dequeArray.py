class DequeArray:

    def __init__(self):
        self.data = [None]
        self.start = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def add_first(self, element):
        if self.size == len(self.data):
            self.increaseSize(2 * len(self.data))
        self.start = (self.start - 1) % len(self.data) #Atualizar um novo um novo início
        self.data[self.start] = element
        self.size += 1

    def add_last(self, element):
        if self.size == len(self.data):
            self.increaseSize(2 * len(self.data))
        last = (self.start + self.size) % len(self.data) #Atualizar um novo final
        self.data[last] = element
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise ValueError("The deque is empty!")
        
        first = self.data[self.start]
        self.data[self.start] = None
        self.start = (self.start + 1) % len(self.data) #Atualizar um novo início depois de remover o início anterior
        self.size -= 1

        if 0 < self.size < len(self.data) // 2:
            self.increaseSize(len(self.data) // 2)

        return first
    
    def remove_last(self):
        if self.is_empty():
            raise ValueError("The deque is empty!")
        
        last = (self.start + self.size - 1) % len(self.data) #Descobrir o final
        value = self.data[last]
        self.data[last] = None
        self.size -= 1

        if 0 < self.size < len(self.data) // 2:
            self.increaseSize(len(self.data) // 2)

        return value
    
    def first(self):
        if self.is_empty():
            raise ValueError("The deque is empty!")
        
        return self.data[self.start]
    
    def last(self):
        if self.is_empty():
            raise ValueError("The deque is empty!")
        
        last = (self.start + self.size - 1) % len(self.data)
        return self.data[last]

    def is_empty(self):
        return len(self.data) == 0
    
    def increaseSize(self, newSize):
        oldData = self.data
        self.data = [None] * newSize
        position = self.start
        for c in range(self.size):
            self.data[c] = oldData[position]
            position = (1 + position) % len(oldData)
        self.start = 0
