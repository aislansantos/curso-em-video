'''
Exercício Python 071:
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

while True:
    valor = int(input('Digite um valor do saque: R$ '))

    mod_cinquenta = int(valor % 50)
    saque_cinquenta = valor - mod_cinquenta
    notas_cinquenta = int(valor / 50)

    valor_vinte = valor - saque_cinquenta

    mod_vinte = int(valor_vinte % 20)
    saque_vinte = valor_vinte - mod_vinte
    notas_vinte = int(valor_vinte / 20)

    valor_dez = valor_vinte - saque_vinte

    mod_dez = int(valor_dez % 10)
    saque_dez = valor_dez - mod_dez
    notas_dez = int(valor_dez / 10)
    
    notas_hum = valor_dez - saque_dez

    
    break
    
print(f'Total de {notas_cinquenta} notas de R$ 50,00')
print(f'Totak de {notas_vinte} notas de R$ 20,00')
print(f'Total de {notas_dez} notas de R$ 10,00')
print(f'total de {notas_hum} notas de R$ 1,00')

print()
print('{:-^150}'.format(' FIM '))
print()
