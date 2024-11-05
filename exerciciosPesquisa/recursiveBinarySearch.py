class RecursiveBinarySearch:
    
    def __init__(self):
        self.list = [2, 3, 4, 5, 6, 8, 9 ,10 ,11, 12, 13]
        self.start = 0
        self.end = len(self.list)

    def recursiveSearch(self, element):
        middle = (self.start + self.end) // 2
        if self.start >= self.end:
            print("Elemento não encontrado!")
            return None
        elif self.list[middle] == element:
            print("Elemento encontrado! ")
            return True
    
        elif self.list[middle] > element:
            self.end = middle
            return self.recursiveSearch(element)

        else:
            self.start = middle + 1
            return self.recursiveSearch(element)
        
    
    def main(self):
        self.recursiveSearch(15)
    
if __name__ == "__main__":
    r = RecursiveBinarySearch()
    r.main()