'''
Exercício Python 044:
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:=^100}'.format(' LOJAS AISLAN ')) #acento circunflexo centraliza no case de formatação nesse caso com 40 espaços, colocando o simbolo de igual "=" . 
print()

print('- valor do Produto -')
preço = float(input('Valor do Produto: R$ '))

print()
print('-------------------------------')
print('|  - Condições de pagamento - |')
print('| 1 - Dinheiro/Cheque (-10%)  |')
print('| 2 - À vista Cartão (-5%)    |')
print('| 3 - 2 x Cartão              |')
print('| 4 - 3 ou mais cartão (+20%) |')
print('-------------------------------')

print()

condição = int(input('Digite a condição: '))

if condição == 1:
    valor_final = preço - ((preço * 10) / 100)
    print('O valor da sua compra será R$ {:.2f}'.format(valor_final))
elif condição ==2:
    valor_final = preço - ((preço * 5) / 100)
    print(' O valor da sua compra é R$ {:.2f}'.format(valor_final))
elif condição == 3:
    valor_final = preço
    valor_parcela = valor_final / 2
    print('O valor total da sua compra será de R$ {:.2f}, e sua parcela será de R$ {:.2f}'.format(valor_final, valor_parcela))
elif condição == 4:
    valor_final = preço + ((preço * 20) / 100)
    total_parcela = int(input('Quantas parcelas: '))
    valor_parcela = valor_final / total_parcela
    print('O total da sua compra será de R$ {:.2f}, em {} parcelas, o valor da sua parcela será de R$ {:.2f}.'.format(valor_final, total_parcela, valor_parcela))
else:
    print()
    print('\033[31mOpção Inválida !\033[m')


print()
print('{:=^100}'.format(' FIM '))
print()
