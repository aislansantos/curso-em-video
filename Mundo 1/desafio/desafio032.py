'''
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

print()
print('-='*25 + ' Ano Bisexto ' + '=-'*25)
print()

from datetime import date

ano = int(input('Digite um ano: '))
if ano == 0: # Pega ano atual se digitar 0
    ano = date.today().year
print (ano % 4)
print (ano % 100)
print (ano % 400)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bisexto'.format(ano))
else:
    print('O ano de {} não é bisexto'.format(ano))


print()
print('-='*25 + ' Selecionando Maior Número ' + '=-'*25)
print()
