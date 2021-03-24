'''
Exercício Python 070:
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

total = caros = contador_caros = contador = preco_barato = 0
barato = ''

while True:
    print('-'*50)
    print('{:^50}'.format('LOJAS BARATÃO'))
    print('-'*50)
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preco do produto: '))

    total += preco
    if preco > 1000:
        caros += preco
        contador_caros += 1

    if contador == 0:
        barato = produto
        preco_barato = preco

    if preco < preco_barato:
        preco_barato = preco
        barato = produto


    opcao = str(input('Deseja continuar[s/n]: ')).strip().lower()
        
    if opcao == 'n' or opcao == 'nao' or opcao == 'não':
        break

    

print(f'o valor total dos itens é R$ {total:.2f}')
print(f'A soma dos {contador_caros} produtos que cutam mais de R$ 1.000 é R$ {caros:.2f}')
print(f'O produto mais barato dos cadastrador é {barato} e custa R$ {preco_barato:.2f}')

print()
print('{:-^150}'.format(' FIM '))
print()
