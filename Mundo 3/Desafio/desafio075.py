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

for cont in n:
    if cont == 9:
        nove += 1
if nove > 0:
    print(f'O numero 9 foi digitado {nove} vezes')
else:
    print(f'O numero 9 não foi Digitado !')

tres = 0
for cont in n:        
    if cont == 3:
        print(f'O numero 3 apareceu a primeira vez na posição {n.index(3)}')
        tres += 1
        break
if tres == 0:
    print('O numero 3 não foi digitado !')



par = 0
for x in range(0, len(n)):
    if n[x] % 2 == 0:    
        par += 1
        
if par == 1:
    print('o numero par digitado foi: ', end='')
    for x in range(0, len(n)):
        if n[x] % 2 == 0:
            print(f'{n[x]}', end='')
            print('.')
elif par > 1:
    print('os numero pares digitados foram: ', end='')
    for x in range(0, len(n)):
        if n[x] % 2 == 0:
            print(f'{n[x]}', end='')
            print('.')
    
    
    
            
print()
print('{:-^150}'.format(' FIM '))
print()
