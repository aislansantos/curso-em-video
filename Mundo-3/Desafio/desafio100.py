'''


'''
import os #Importa biblioteca do sistema
from random import randint
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio 100 '))
print()

def sorteia(lista):
    print('SORTEANDO 5 VALORES DA LISTA:', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def soma_Par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
soma_Par(numeros)

print()
print('{:-^150}'.format(' FIM '))
print()

