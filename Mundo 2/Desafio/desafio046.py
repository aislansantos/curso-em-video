'''
Exercício Python 046:
Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
'''
import os #Importa biblioteca do sistema
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa


print()
print('{:=^150}'.format(' Contagem Regressiva '))
print()

for c in range(10, 0-1, -1):
    print(c)
    sleep(1)

print('fogos detonados!!!')

print()
print('{:=^150}'.format( ' Fim '))
print()
