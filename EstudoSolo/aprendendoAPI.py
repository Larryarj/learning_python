import requests

def fetchdata(endpoint):
    response = requests.get(f"https://rickandmortyapi.com/api/{endpoint}")

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar informação de {endpoint} : {response.status_code}")
        return None

def GetCharacterbyName(name):
    characters = fetchdata("character")
    if characters:
        for character in characters['results']:
            if name.lower() in character['name'].lower():
                print(character["name"]) 
    return None

def Getallcharactersname():

    characters = fetchdata("character")
    if characters:
        for character in characters['results']:
            print(character["name"])
    return

def main():
    print("aprendendo a mexer em API, com a api do rick and morty")

    while True:
        acao = input("digite 1 para buscar todos os personagens,\n" 
                    "digite 2 para buscar um personagem pelo nome,\n"
                    "digite 3 para ver o nome de todos os personagens\n"
                    "Ou digite qualquer coisa para sair:")

        match acao:

            case "1":
                print(fetchdata("character"))

            case "2":
                nomebusca = input("digite o nome do personagem que deseja buscar: ")
                print(GetCharacterbyName(nomebusca))

            case "3":
                print(Getallcharactersname())

            case _:
                break

main()
