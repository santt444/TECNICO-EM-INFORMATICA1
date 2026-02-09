numeros = [] 
 
def adicionar_numero(): 
    numero = int(input("Digite um número: ")) 
    numeros.append(numero) 
 
def listar_numeros(): 
    print(numeros[0]) 
 
adicionar_numero() 
listar_numeros() 
 