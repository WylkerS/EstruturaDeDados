class BinarySearch:

    def __init__(self):
        self.list = ["Abacaxi", "Banana", "Carambola", "Damasco", "Erva"]

    def search(self, element):
        start = 0
        end = len(self.list)

        while start < end:
            middle = (start + end) // 2
            if self.list[middle] == element:
                print("Elemento encontrado!")
                return True

            elif self.list[middle] > element:
                end = middle
            
            else:
                start = middle + 1

        print("Elemento não encontrado!")


    def main(self):
        self.search("Erva")


if __name__ == "__main__":
    b = BinarySearch()
    b.main()