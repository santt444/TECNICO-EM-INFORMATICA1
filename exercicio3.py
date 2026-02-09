notas = [] 
 
def adicionar_nota(): 
    nota = float(input("Digite a nota: ") )
    notas.append(nota) 
 
def calcular_media(): 
    media = sum(notas) / len(notas) 
    print("Média:", media) 
 
adicionar_nota() 
adicionar_nota() 
calcular_media() 
 