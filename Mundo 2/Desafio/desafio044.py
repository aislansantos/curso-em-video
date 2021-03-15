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
print('-='*25 + ' Calculo de Venda ' + '=-'*25)
print()

print('- valor do Produto -')
preço = float(input('Valor do Produto: R$ '))

print()
print('-------------------------------')
print('|  - Condição de pagamento -  |')
print('| 1 - Dinheiro/Cheque (-10%)  |')
print('| 2 - À vista Cartão (-5%)    |')
print('| 3 - 2 x Cartão              |')
print('| 4 - 3 ou mais cartão (+20%) |')
print('-------------------------------')

condição = int(input('Digite a condição: '))

if condição == 1:
    valor_final = preço - ((preço * 10) / 100)
    print('R$ {:.2f}'.format(valor_final))
elif condição ==2:
    valor_final = preço - ((preço * 5) / 100)
    print('R$ {:.2f}'.format(valor_final))
elif condição == 3:
    valor_final = preço
elif condição == 4:
    valor_final = preço + ((preço * 20) / 100)
    print('R$ {:.2f}'.format(valor_final))
else:
    print('Opção Inválida !')


print()
print('-='*25 + ' FIM' + '=-'*25)
print()
