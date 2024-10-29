class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None


class ListaEncadeadaCircular:
    def __init__(self):
        self.inicio = None
        self.atual = None

    def adicionar_membro(self, nome):
        novo_membro = Membro(nome)
        if not self.inicio:
            self.inicio = novo_membro
            novo_membro.proximo = novo_membro  
            self.atual = novo_membro
        else:
            novo_membro.proximo = self.inicio
            self.atual.proximo = novo_membro
            self.atual = novo_membro

    def remover_membro(self, nome):
        if not self.inicio:
            print(f"Membro {nome} não encontrado na lista.")
            return

        atual = self.inicio
        anterior = None
        while True:
            if atual.nome == nome:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    
                    self.atual = self.atual.proximo if self.atual == self.inicio else self.atual
                    
                    if self.inicio == atual:
                        self.inicio = atual.proximo
                    else:
                        ultimo = self.inicio
                        while ultimo.proximo != self.inicio:
                            ultimo = ultimo.proximo
                        ultimo.proximo = self.inicio
                print(f"Membro {nome} removido da lista.")
                return
            anterior = atual
            atual = atual.proximo
            if atual == self.inicio:
                break

        print(f"Membro {nome} não encontrado na lista.")

    def proximo_responsavel(self):
        if not self.inicio:
            return None
        self.atual = self.atual.proximo
        return self.atual.nome

    def mostrar_lista(self):
        if not self.inicio:
            print("Lista vazia.")
            return
        atual = self.inicio
        resultado = []
        while True:
            resultado.append(atual.nome)
            atual = atual.proximo
            if atual == self.inicio:
                break
        print(" -> ".join(resultado) + " -> (volta para " + self.inicio.nome + ")")


# Funções de teste
def test_adicionar_membros():
    lista = ListaEncadeadaCircular()
    
    lista.adicionar_membro("Abel")
    lista.adicionar_membro("Bia")
    lista.adicionar_membro("Carlos")
    
    print("Teste de Adição de Membros:")
    print("Lista após a adição:")
    lista.mostrar_lista()
    
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Abel
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Bia
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Carlos
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Abel


def test_remover_membros():
    lista = ListaEncadeadaCircular()
    
    lista.adicionar_membro("Abel")
    lista.adicionar_membro("Bia")
    lista.adicionar_membro("Carlos")
    
    print("Teste de Remoção de Membros:")
    lista.remover_membro("Bia")  # Remover Bia
    print("Lista após a remoção de Bia:")
    lista.mostrar_lista()
    
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Carlos
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Abel


def test_proximo_responsavel():
    lista = ListaEncadeadaCircular()
    
    lista.adicionar_membro("Abel")
    lista.adicionar_membro("Bia")
    lista.adicionar_membro("Carlos")
    
    print("Teste de Próximo Responsável:")
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Abel
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Bia
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Carlos
    print("Próximo responsável:", lista.proximo_responsavel())  # Espera-se Abel


def main():
    test_adicionar_membros()
    test_remover_membros()
    test_proximo_responsavel()

if __name__ == "__main__":
    main()
