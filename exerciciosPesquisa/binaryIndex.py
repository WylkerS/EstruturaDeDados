class BinaryIndex:
    
    def __init__(self):
        self.list = [1, 2, 4, 4, 4, 5]
        self.index = []

    def search(self, element):
        start = 0
        end = len(self.list)

        while start < end:
            middle = (start + end) // 2

            if self.list[middle] == element: 
                index = middle
                while index >= 0 and self.list[index] == element:
                    self.index.append(index)
                    index -= 1
                
                index = middle + 1
                while index <= end - 1 and self.list[index] == element:
                    self.index.append(index)
                    index += 1
                
                self.index.sort()
                print(f"Elemento encontrado nos índices {self.index}")

                return None

            elif self.list[middle] > element:
                end = middle
            
            else:
                start = middle + 1

        print("Elemento não encontrado!")


    def main(self):
        self.search(4)


if __name__ == "__main__":
    b = BinaryIndex()
    b.main()