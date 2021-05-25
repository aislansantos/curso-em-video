'''
Exercício Python 066:
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

s = c  = 0

while True:
    n = int(input('Digie um número[999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} numeros é = {s}')

print()
print('{:-^150}'.format(' FIM '))
print()
