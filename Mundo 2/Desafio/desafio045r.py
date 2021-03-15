'''
Desafio 045 resolvido conforme Guanabara
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa
from random import randint
from time import sleep

# Seção que faz a escolha aleatória pelo computador
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('{:-^40}'.format(' Exercicio Jokenpô Resolvido '))
print()
print(''' Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=-' * 10)
print('O compurador jogou {}!'.format(itens[computador])) # No format mostramos como mostrar por escrito a opção como um texto dentro de itens ao invés de numero, no format da variável.
print('Jogador jogou {}!'.format(itens[jogador]))
print('-=-' * 10)
# Resolvendo por forma de condição aninhadas
if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # Computador jogou Tesoura
    if jogador == 0:
            print('JOGADOR VENCE!')
    elif jogador == 1:
            print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')

print()
print('{:-^40}'.format('Fim'))
