# POO software de gerenciamento de contas bancarias

# atualizaçao: adicionados metodos de: depositar na conta, sacar da conta. removido metodo de ver saldo da conta.

# ================================

# classe para instanciar contas
class Conta:
    def __init__(self, idconta, nome, saldo):
        self.idconta = idconta
        self.nome = nome
        self.saldo = saldo

    def visualizar(self):
        print(f"Numero da conta: {self.idconta}, nome da conta: {self.nome}, saldo da conta: {self.saldo}")

# classe para alterar contas
class Banco:
    def __init__(self):
        self.DBbanco = []

    def addconta(self, contatoadd):
        self.DBbanco.append(contatoadd)
        print('Conta adicionada ao banco.')
        #pirntar conta criada

    def removerconta(self, id):
        for conta in self.DBbanco:
            if conta.idconta == id:
                self.DBbanco.remove(conta)
                print('Conta removida do banco')
                return
        print('conta inexistente.')

    def detalharconta(self, id):
        for conta in self.DBbanco:
            if conta.idconta == id:
                conta.visualizar()
                return
        print('conta inexistente.')

    def vercontas(self):
        for conta in self.DBbanco:
            print(f"Conta: {conta.nome}")
        if len(self.DBbanco) == 0:
            print('nenhuma conta no banco.')

    def deposito(self, id, qtdtoadd):
        for conta in self.DBbanco:
            if conta.idconta == id:
                conta.saldo += qtdtoadd
                print(f'depósito de {qtdtoadd} efetuado da conta: {conta.nome}')
                return

    def saque(self, id, qtdtorem):
        for conta in self.DBbanco:
            if conta.idconta == id:
                conta.saldo -= qtdtorem
                print(f'saque de {qtdtorem} efetuado da conta: {conta.nome}')
                return

def main():

    bancocentral = Banco()
    nextid = 1
    contaLa = Conta(str(nextid), 'fulano', 1000.0)
    bancocentral.addconta(contaLa)

    while True:
        print('--'*20)
        act = input("o que deseja fazer? digite:\n"
                    "1 para adicionar conta ao banco\n"
                    "2 para remover conta do banco\n"
                    "3 para ver informações de uma conta\n"
                    "4 para ver as conta no banco\n"
                    "5 para fazer um depósito\n"
                    "6 para faze um saque\n"
                    "Ou digite qualquer coisa para sair: ")
        print('--'*20)

        match act:
            case '1':
                print('criando a conta')
                nextid += 1
                contaobj = Conta(
                    str(nextid),
                    input("digite o nome da conta: "),
                    float(input("digite o saldo de entrada: "))
                )
                bancocentral.addconta(contaobj)

            case '2':
                idacctoremove = input('digite o id da conta para apagar: ')
                bancocentral.removerconta(idacctoremove)

            case '3':
                id_conta_detalhar = input('digite o número da conta para ver suas informações: ')
                bancocentral.detalharconta(id_conta_detalhar)

            case '4':
                bancocentral.vercontas()

            case '5':
                iddeposito = input('digite o numero da conta que voce deseja fazer um deposito: ')
                qtddeposito = float(input('digite quanto voce vai depositar: '))
                bancocentral.deposito(iddeposito, qtddeposito)

            case '6':
                idsaque = input('digite o numero da conta que voce deseja fazer um saque: ')
                qtdsaque = float(input('digite quanto voce vai sacar: '))
                bancocentral.saque(idsaque, qtdsaque)

            case _:
                print("sistema encerrado.")
                break

main()
