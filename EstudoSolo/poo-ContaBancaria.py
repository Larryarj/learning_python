# POO software de gerenciamento de contas bancarias

# atualizaçao: adicionados metodos de: ver detalhes de uma conta, ver contas no banco e ver saldo de conta

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

    def removerconta(self, id):
        for conta in self.DBbanco:
            if conta.idconta == id:
                self.DBbanco.remove(conta)
                print('Conta removida do banco')
                return
        print('conta inexistente.')

    def detalharconta(self, nome):
        for conta in self.DBbanco:
            if conta.nome == nome:
                conta.visualizar()

    def vercontas(self):
        for conta in self.DBbanco:
            print(f"Conta: {conta.nome}")
        if len(self.DBbanco) == 0:
            print('nenhuma conta no banco')

    def versaldo(self, id):
        for conta in self.DBbanco:
            if conta.idconta == id:
                print(f"saldo da conta {conta.nome}: {conta.saldo}")
                return

def main():

    bancocentral = Banco()
    nextid = 1
    conta1 = Conta(str(nextid), 'fulano', 1000.0)
    bancocentral.addconta(conta1)

    while True:
        print('--'*20)
        act = input("o que deseja fazer? digite:\n" \
                    "1 para adicionar conta ao banco\n" \
                    "2 para remover conta do banco\n" \
                    "3 para ver detalhes de uma conta\n" \
                    "4 para ver saldo de conta\n" \
                    "5 para ver as conta no banco\n" )
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
                conta_detalhar = input('digite o nome da conta para ver detalhes: ')
                bancocentral.detalharconta(conta_detalhar)

            case '4':
                id = input('digite o id da conta para ver o saldo: ')
                bancocentral.versaldo(id)

            case '5':
                bancocentral.vercontas()

            case _:
                print("sistema encerrado.")
                break

main()
