'''
Exercício Python 051:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:=^150}'.format(' 10 TERMOS DE UMA PA '))
print()

primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')

print()
print('{:=^150}'.format(' FIM '))
print()
