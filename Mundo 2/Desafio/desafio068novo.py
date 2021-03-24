'''
Exercício Python 068:
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
'''
import os #Importa biblioteca do sistema
from random import randint
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()
jogada = ''
while True:
    computador = randint(0, 1)
    numero_jogador = int(input('Qual o numero você escolhe ?'))
    total = (computador + numero_jogador) % 2
    print(total)    
    if total == 0:
        jogada = 'P'
    elif total == 1:
        jogada = 'I'
    jogador = str(input('Par ou Impar[P/I]: ')).strip().upper()
    if jogador == jogada:
        print('você Venceu !')
    elif jogador != jogada:
        print('Computador ganhou!')
        break

print()
print('{:-^150}'.format(' FIM '))
print()
