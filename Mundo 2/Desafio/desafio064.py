'''
Exercício Python 064:Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

soma = n = contador = 0

n = int(input('Digite um numero para somar[999 para parar]: '))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um numero para somar[999 para parar]: '))

print('você digitou {} numeros e a soma entre eles foi {}'.format(contador ,soma))

print()
print('{:-^150}'.format(' FIM '))
print()
