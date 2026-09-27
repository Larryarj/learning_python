# Sofrware de gerenciamento de uma concessionária

# ATUALIZAÇÃO: implementado a classe (concessionaria)

# ===========================================



# classe para criar objetos(carros)
class Carro:
    def __init__(self, id,marca, modelo, ano, quilometragem):# método construtor
        # atributos de instância
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    # método()
    def apresentar(self):
        print(f"id: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, quilometragem: {self.quilometragem}")


# classe para gerenciar carros da concessionaria
class concessionaria:
    def __init__(self): # método construtor
        # atributos de instância
        self.tabela_carros = []

    # método()
    def adicionar_carro(self, carro):
        self.tabela_carros.append(carro)
        print("carro adicionado a garagem.")

    # método()
    def retirar_carro(self, id):
        for carro_item in self.tabela_carros:
            if carro_item.id == id:
                self.tabela_carros.remove(carro_item)
                print(f"carro {carro_item.modelo} removido com sucesso.")
                return
        print("carro não encontrado")

    # método()
    def listar_carros(self):
        if len(self.tabela_carros) == 0:
            print("tabela de carros vázia.")
        else:
            for carro_item in self.tabela_carros:
                print(carro_item.modelo)


def main ():

    concessionaria1 = concessionaria()
    proximo_id = 1
    civic = Carro('1', 'honda', 'civic', 2009, 87731.6)
    concessionaria1.adicionar_carro(civic)

    while True:
        print('--' * 20)
        acao = input("1 - Para ver os carros disponiveis\n"
                     "2 - Para adicionar um carro \n"
                     "3 - Retirar um carro\n"
                     "ou digite qualquer coisa para sair\n")
        print('--' * 20)

        match acao:
            case '1':
                concessionaria1.listar_carros()

            case '2':
                # carroobj = Carro(input("Digite a marca do carro: "),
                #               input("Digite o modelo do carro: "),
                #               input("Digite o ano do carro: "),
                #               input("Digite a quilometragem do carro: "))

                marca = input("Digite a marca do carro: ")
                modelo = input("digite o modelo do carro: ")
                ano = int(input("digite o ano do carro: "))
                quilometragem = float(input("digite a quilometragem do carro: "))

                carroobj = Carro(str(proximo_id), marca, modelo, ano, quilometragem)
                proximo_id += 1
                concessionaria1.adicionar_carro(carroobj)

            case '3':

                modelo_retirar = input("Digite o modelo do carro que deseja retirar: ")
                print(f"tosdos os carros com o modelo {modelo_retirar} são: ")
                
                for carro_item in concessionaria1.tabela_carros:
                    if carro_item.modelo == modelo_retirar:
                        carro_item.apresentar()

                id_carro_obj_a_retirar = input("Digite o ID do carro que deseja retirar? ")
                concessionaria1.retirar_carro(id_carro_obj_a_retirar)

            case _:
                break

main()
