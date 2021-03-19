'''
Exercício Python 055:
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

menor = 100000000000000000000000
maior = 0
erro = 0

for pessoa in range(1, 6):
    peso = float(input('Digite o peso de {}ª pessoa: '.format(pessoa)))
    if peso < 332:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
    else:
        erro += 1

if erro > 0:
    print('{:-^150}'.format('Erro'))
    print('passou o peso de Manuel Uribe a pessoa mais pesada do guiness de 332 Kg - existe {} lançamento de peso errado'.format(erro))
print('{:-^150}'.format('Totais'))
print('A pessoa mais leve pesa {} quilos'.format(menor))
print('A pessoa mais pesada pesa {} quilos'.format(maior))

print()
print('{:-^150}'.format(' FIM '))
print()
