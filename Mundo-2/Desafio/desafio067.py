'''
Exercício Python 067:
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

while True:
    c = 0
    n = int(input('Digite qual tabuada deseja: '))
    if n <= 0:
        break
    os.system('cls')
    print(f'A tabuada do {n} é:')
    while c <= 10:
        tabuada = c * n
        print(f'{c:2} * {n} = {tabuada}')
        c += 1

     

print()
print('{:-^150}'.format(' FIM '))
print()
