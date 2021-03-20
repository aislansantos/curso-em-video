'''
Exercício Python 060:
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Fatorial '))
print()

n = int(input('Digite um número para calcular seu fatorial '))
numero = n
fatorial = 1


while n > 0:
    fatorial = fatorial * n
    n -= 1
print('O fatorial de {}! é = {}'.format(numero, fatorial))
    

print()
print('{:-^150}'.format(' FIM '))
print()
