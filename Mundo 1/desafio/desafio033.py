'''
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

print()
print('-='*25 + ' Selecionando Maior Número ' + '=-'*25)
print()

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi {}'.format(menor))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor digitado foi {}'.format(maior))

print()
print ('-='*30 + ' FIM ' + '=-'*30)
