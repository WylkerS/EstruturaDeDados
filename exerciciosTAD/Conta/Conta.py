#Crie um tipo de dados Conta quearmazena 'numero_conta', 'nome_correntista', 'saldo'
#Pergunteao usuário vários números decontas e os armazenem uma lista
#Após armazenar,escreva todas as contas na tela
#Escreva a conta com o maior saldo

class Conta:
    
    def __init__(self, num, nome, saldo):
        self.num = num
        self.nome = nome
        self.saldo = saldo

    def armazenaContas():
        listaContas = []
        while True: 
            numConta = int(input("\nNúmero da conta ou '0' para sair: "))
            if numConta == 0:
                break
            nomeCorrentista = input("Nome do correntista: ")
            saldoConta = float(input("Saldo da conta: "))
            listaContas.append(Conta(numConta, nomeCorrentista, saldoConta))
            
        return listaContas
        
    def exibirContas(contas):
            print("\nTodas as contas")
            for c in contas:
                print(f"\nNúmero: {c.num}\nNome: {c.nome}\nSaldo: R$ {c.saldo:.2f}")

    def maiorSaldo(contas):
        maiorSaldo = contas[0]
        for c in contas:
            if c.saldo > maiorSaldo.saldo:
                maiorSaldo = c
        return maiorSaldo


contas = Conta.armazenaContas()
Conta.exibirContas(contas)
saldoMaior = Conta.maiorSaldo(contas)
print(f"\nA conta de maior saldo é\n\nNúmero: {saldoMaior.num}\nNome: {saldoMaior.nome}\nSaldo: {saldoMaior.saldo}")