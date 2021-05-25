'''
Exercício Python 047:
Crie um programa que mostre na tela todos os números
pares que estão no intervalo entre 1 e 50.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Números Pares '))
print()

for c in range(2, 51, 2):
        print(c, end=' ')
print('Pronto')
print()
print('{:-^150}'.format(' Fim '))
print()
