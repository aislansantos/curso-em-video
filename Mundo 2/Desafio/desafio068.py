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

c = 0
while True:
    jogada = randint(0, 1)
    jogador = str(input('Par ou Impar?[P/I]: ')).strip().upper()
    if jogador == 'PAR' or jogador == 'P':
        jogador = 0
    elif jogador == 'IMPAR' or jogador == 'I':
        jogador = 1

    
    if jogador == jogada:
        print('Você ganhou !')
    elif jogador != jogada:
        print('Computador ganhou !')
        break
    
    c += 1

if c == 0:
    print('Não ganhou nenhuma! melhor sorte na proxima')
elif c == 1:
    print(f'Voce ganhou {c} vez')
else:
    print(f'Voce ganhou {c} vezes')

print()
print('{:-^150}'.format(' FIM '))
print()
