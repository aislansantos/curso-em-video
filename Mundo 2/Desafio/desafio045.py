'''
Exercício Python 045:
Crie um programa que faça o computador jogar Jokenpô com você.
'''
import os #Importa biblioteca do sistema
from random import randint #importa biblioteca de numeros randomicos
from time import sleep # importa a biblioteca de tempo
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('-='*25 + ' Jokenpô ' + '=-'*25)
print()

print('0 - PEDRA')
print('1 - PAPEL')
print('2 - TESOURA')
print()

opcao_computador = randint(0,2)
opcao_jogador = int(input('Digite sua escolhar: '))
print()

if opcao_jogador == 0:
    opcao_jogador = 'PEDRA'
elif opcao_jogador == 1:
    opcao_jogador = 'PAPEL'
elif opcao_jogador == 2:
    opcao_jogador = 'TESOURA'

if opcao_computador == 0:
        opcao_computador = 'PEDRA'
elif opcao_computador == 1:
    opcao_computador = 'PAPEL'
elif opcao_computador == 2:
    opcao_computador = 'TESOURA'
    
print('o computador escolheu {}'.format(opcao_computador))
print('Você escolheu {}'.format(opcao_jogador))

if opcao_computador == 'PEDRA' and opcao_jogador == 'PEDRA' or opcao_computador == 'PAPEL' and opcao_jogador =='PAPEL'  or opcao_computador == 'TESOURA' and opcao_jogador == 'TESOURA':
    print('Jogo emptatado !')
elif opcao_computador == 'PEDRA' and opcao_jogador == 'TESOURA' or opcao_computador == 'PAPEL' and opcao_jogador == 'PEDRA' or opcao_computador == 'TESOURA' and opcao_jogador == 'PAPEL':
    print('Seu adversario ganhou!')
else:
    print('Você ganhou !')

print()
print('-='*25 + ' FIM' + '=-'*25)
print()
