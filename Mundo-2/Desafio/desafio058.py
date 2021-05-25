'''
Exercício Python 058:
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa
from random import randint

print()
print('{:-^150}'.format(' Exercicio '))
print()

computador = randint(0, 10)
print('Sou seu computador ... acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi ?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ?'))
    palpite += 1
    if jogador == computador:
        acertou = True
    if jogador < computador:
        print('mais ... Tente mais uma  vez.')
    else:
        print('menos ... Tente mais uma  vez.')

print('Acertou, com {} palpites'.format(palpite))

print()
print('{:-^150}'.format(' FIM '))
print()
