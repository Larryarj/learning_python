# ================= programação orientada a objetos ====================

# Classe: O professor utiliza a analogia de uma "forminha de biscoito" ou "planta baixa de uma casa" 
# para explicar que a classe é o modelo ou molde que define o padrão para a criação de objetos.

# Objeto: É a instância(item) física ou abstrata criada a partir de uma classe. Um objeto possui características, comportamentos e um estado próprio.

# Atributos: São as características do objeto (ex: tamanho, cor, peso).
# Métodos: São as ações que o objeto pode realizar ou que podem ser feitas com ele (ex: cozinhar, congelar, comer).

# Instanciamento: O processo de criar um objeto real seguindo o modelo definido pela classe.

# Estado de um Objeto: Refere-se ao conjunto atual de valores dos atributos de um objeto em um determinado momento.

# Objetos abstratos: Ex: Processo de venda: Tem atributos como valor e produto, e métodos como iniciar venda ou processar pagamento 





# Sofrware de gerenciamento de uma concessionária
# versão básica
# ==============================================

# classe para criar objetos(carros)
class Carro:

    def __init__(self, id, marca, modelo, ano, quilometragem): # método construtor
        # atributos de instância
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    # métodos()
    def apresentar(self):
        print(f"id: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, quilometragem: {self.quilometragem}")

def retirarcarro(indentificador, tabela):
    for carro_item in tabela:
        if carro_item.id == indentificador:
            tabela.remove(carro_item)
            print(f"Carro {carro_item.modelo} de id: {indentificador}. removido com sucesso.")
            return

    print("id não encontrado")

corolla = Carro('1', "Toyota", "corolla", 2020, 50000.0)
# corolla.apresentar()
tabela_carros = [corolla]
proximo_id = 1

def main ():

    while True:
        print('--' * 20)
        acao = input("1 - Para ver os carros disponiveis\n"
                     "2 - Para adicionar um carro \n"
                     "3 - Retirar um carro\n"
                     "ou digite qualquer coisa para sair\n")
        print('--' * 20)

        match acao:
            case '1':

                for carro_item in tabela_carros:
                    print(carro_item.modelo)

                if len(tabela_carros) == 0:
                    print("tabela de carros vázia.")

            case '2':
                # carro = Carro(input("Digite a marca do carro: "),
                #               input("Digite o modelo do carro: "),
                #               input("Digite o ano do carro: "),
                #               input("Digite a quilometragem do carro: "))

                marca = input("Digite a marca do carro: ")
                modelo = input("digite o modelo do carro: ")
                ano = int(input("digite o ano do carro: "))
                quilometragem = float(input("digite a quilometragem do carro: "))

                carroobj = Carro(str(proximo_id + 1), marca, modelo, ano, quilometragem)
                tabela_carros.append(carroobj)
                proximo_id += 1

            case '3':
                modelo_retirar = input("Digite o modelo do carro que deseja retirar: ")

                if modelo_retirar in [carro.modelo for carro in tabela_carros]:

                    print(f"tosdos os carros com o modelo {modelo_retirar} são: ")

                    for carro_item in tabela_carros:
                        if carro_item.modelo == modelo_retirar:
                            carro_item.apresentar()

                else:
                    print("Carro não encontrado na tabela.")

                carro_obj_a_retirar = input("Digite o ID do carro que deseja retirar? ")
                retirarcarro(carro_obj_a_retirar, tabela_carros)

            case _:
                break

main()
