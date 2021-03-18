'''
Exercício Python 050:
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' SOMA NUMEROS PARES '))
print()

soma = 0
for c in range(0, 6 ):
   n = int(input('Digite um número: '))
   if n % 2 == 0:
     soma = soma + n
print(soma)

print()
print('{:-^150}'.format(' FIM '))
print()
