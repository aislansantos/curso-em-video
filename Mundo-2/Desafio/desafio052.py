'''
Exercício Python 052:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:=^150}'.format(' NÚMEROS PRIMOS '))
print()

numero = int(input('Digite um número: '))
contador = 0

for c in range(1, numero + 1):
    divisao = numero % c
    if divisao == 0:       
        contador = contador + 1

print()
if contador == 2:  
   print('É número primo !')
else:    
     print('Não é numero Primo! o numero foi divisivel por {} numeros'.format(contador))


print()
print('{:=^150}'.format(' FIM '))
print()
