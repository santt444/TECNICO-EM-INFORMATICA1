usuario = int(input('digite um número: '))

if usuario < 0:
    print(' essse número é negativo ')

elif usuario > 0:
    print(' esse número é positivo ')

else:
    print(' igual a zero ')

print('_' * 20)

for numero in range (1, 21):
    print(numero)
    
print('_' * 20)

numero = int(input("Digite um número: "))

i = 0
while i <= numero:
    print(i)
    i += 1

print('_' * 20)

while True:
    usuario = input("Digite uma palavra: ")
    if usuario.lower() == "sair":
        break
    print(f"voce digitou:  {usuario}")
print("Programa enceerrado! ")
print('_' * 20)

cores = ("vermelho", "verde", "roxo", "preto")
print(cores)

i = int(input("escolha um indice de 0 a 3:  "))

if 0 <= i <= 3:
    print(f"cor confirmada: {cores[i]}")
    print('_' * 20)

nomes = []

for i in range (5):
    nome = input(f"digite o {i+1}º nome: ")
    nomes.append(nome)

print("Nomes cadastrados:", nomes)
print("Quantidade de nomes:", len(nomes))
print('_' * 20)

import random 
sorteio = random.randint(1, 10)

chute = int(input("adivinhe o número sorteado (1 a 10): "))

if chute == sorteio:
    print("voce acertou")

else:
    print(f"errou o número era {sorteio}")
print('_' * 20)

total = 10  #  global

def teste_escopo():
    total = 5  #  local existe só dentro da função
    print(f"Dentro da função: {total}")

teste_escopo()

print(f"Fora da função (global){total}: ")
##testando
## som
