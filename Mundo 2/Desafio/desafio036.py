'''
Exercício Python 036:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('-='*25 + ' Aprovar Empréstimo ' + '=-'*25)
print()

valor_casa = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o valor do salário do comprador? R$ '))
anos = int(input('Quanto anos para pagar o imóvel? '))
meses = anos * 12
mensalidade = valor_casa / meses
mensalidade_maxima = (salario * 30) /100


print()
print('O valor do Imovel é de: R$ {:.2f}'.format(valor_casa))
print('O salário mensal do possível comprador é de {:.2f} '.format(salario), end='')
if anos > 1:
    print('Ele vai pagar em {:.0f} anos que são {:.0f} meses'.format(anos, meses))
else:
    print('Ele vai pagar em {:.0f} ano que são {:.0f} meses'.format(anos, meses))

print()
print('O valor da mensalidade é de R$ {:.2f}'.format(mensalidade))


if mensalidade > mensalidade_maxima:
    print('Crédito não liberado! Maximo que ele pode pagar de mensalidade é R$ {:.2f}.'.format(mensalidade_maxima))
else:
    print('O valor da parcela é de R$ {:.2f}, sua parcela pode ser até o valor de R$ {:.2f}, '.format(mensalidade, mensalidade_maxima), end = '')
    print('Aproveite seu novo lar !')

print()
print('-='*28 + ' FIM ' + '=-'*28)
print()
