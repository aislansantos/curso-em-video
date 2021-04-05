'''
Exercício Python 082:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()
numeros = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um valor:'))
    numeros.append(n)
    opcao = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
for p in range(0, len(numeros)):
    if numeros[p] % 2 == 0:
        pares.append(numeros[p])
for i in range(0, len(numeros)):
    if numeros[i] % 2 == 1:
        impares.append(numeros[i])
        
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
print()
print('{:-^150}'.format(' FIM '))
print()

