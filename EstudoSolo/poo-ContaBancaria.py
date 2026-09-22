# POO software de gerenciamento de contas bancarias

# versão inicial

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

def main():

    bancocentral = Banco()
    nextid = 1
    contaLa = Conta(str(nextid), 'fulano', 1000.0)
    bancocentral.addconta(contaLa)

    while True:
        print('--'*20)
        act = input("o que deseja fazer? digite:\n" \
                    "1 para adicionar conta ao banco\n" \
                    "2 para remover conta do banco\n" \
                    "3 para ver detalhes de uma conta\n" )
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

            case _:
                print("sistema encerrado.")
                break
            
main()
