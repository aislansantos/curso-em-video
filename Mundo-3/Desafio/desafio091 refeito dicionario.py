'''
Exercício Python 091:
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
import os  # Importa biblioteca do sistema
from random import randint
from time import sleep
from operator import itemgetter

# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()

print()
print('{:-^150}'.format(' FIM '))
print()
