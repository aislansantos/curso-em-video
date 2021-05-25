'''
Exercício Python 060:
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
nesse exercicio usando o FOR.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

n = int(input('Digite um numero: '))
f = 1

for n in range(n , 1, -1):
    print('{} '.format(n), end='')
    print('-> ' if n > 2 else ' = ', end = '')
    f *= n
print('{} '.format(f))

print()
print('{:-^150}'.format(' FIM '))
print()
