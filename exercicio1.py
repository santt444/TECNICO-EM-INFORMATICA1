nomes = []

def adicionar_nome():
    nome = input("Digite um nome: ")
    nomes.append(nome)

def listar_nomes():
    for nome in nomes:
        print(nome)

adicionar_nome()
listar_nomes()
