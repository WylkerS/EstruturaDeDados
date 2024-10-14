class EmptyQueue(Exception):
    pass

class Queue:



    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.start = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def increaseSize(self, newSize):
        oldData = self.data
        self.data = [None] * newSize
        position = self.start
        for c in range(self.size):
            self.data[c] = oldData[position]
            position = (1 + position) % len(oldData)
        self.start = 0
        self.capacity = newSize

    def enqueue(self, element):
        if self.size == self.capacity:
            self.increaseSize(2 * self.capacity)
        available = (self.start + self.size) % len(self.data)
        self.data[available] = element
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue("The queue is empty!")
    
        result = self.data[self.start]
        self.data[self.start] = None
        self.start = (self.start + 1) % self.capacity
        self.size -= 1

        if 0 < self.size < self.capacity // 4:
            if self.capacity // 2 >= 1: 
                self.increaseSize(self.capacity // 2)

        return result   
    


