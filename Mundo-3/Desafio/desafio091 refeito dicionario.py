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

jogo = dict()
ranking = list()

print()
print('{:-^150}'.format(' Exercicio '))
print()

#Gera quantidade de jogaodres e atribui a jogada a cada um construindo o dicionario
for j in range(0,4):
    jogo['jogador' + str(j+1)] = randint(1, 6)

for k, v in jogo.items():
    print(f'{k}: valor dado {v}')
    sleep(1)

print('{:-^150}'.format(' Ranking '))

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]} pontos.')
    sleep(1)

print()
print('{:-^150}'.format(' FIM '))
print()
