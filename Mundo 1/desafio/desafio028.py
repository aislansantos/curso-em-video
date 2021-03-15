'''
Exercício Python 028: Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
escolhido = randint(0, 5)

numero = int(input('Digite um numero: '))
print('Processando...')
sleep(2)
if numero == escolhido:
    print('Acertou!'.format(escolhido))
else:
    print('ERROU! Pensei no numero {}'.format(escolhido))
