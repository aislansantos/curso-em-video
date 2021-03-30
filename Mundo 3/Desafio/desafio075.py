'''
Exercício Python 075:
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.

'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

n = (int(input('Digite um numero: ')),
    int(input('digite um numero: ')),
    int(input('digite um numero: ')),
    int(input('digite um numero: ')))

print(f'Os numeros digitados foram: {n}')
nove = 0
tres = 0
for cont in n:
    if cont == 9:
        nove += 1
if nove > 0:
    print(f'O numero 9 foi digitado {nove} vezes')
else:
    print(f'O numero 9 não foi Digitado !')

for cont in n:
    if cont == 3:

print()
print('{:-^150}'.format(' FIM '))
print()

