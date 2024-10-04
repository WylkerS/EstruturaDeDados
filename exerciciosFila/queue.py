class EmptyQueue(Exception):
    pass

class Queue:
    
    def __init__(self):
        self.data = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.size = 0
        self.start = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def increasesSize(self, newSize):
        oldData = self.data
        self.data = [None] * newSize
        position = self.start
        
        for c in range(self.size):
            self.data[c] = oldData[position]
            position = (1 + position) % len(oldData)
        self.start = 0
    
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue("The queue is empty!")
        result = self.data[self.start]
        self.data[self.start] = None
        self.start = (self.start + 1) % len(self.data)
        self.size -= 1
        return result
    
    def enqueue(self, value):
        if self.size == len(self.data):
            self.increasesSize(2 * len(self.data))
        available = (self.start + self.size) % len(self.data)
        self.data[available] = value
        self.size += 1

    def first(self):
        return self.data[0]

    