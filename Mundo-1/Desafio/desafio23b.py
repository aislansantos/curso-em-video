'''
Faça um programa que leia um numero de 0 a 9999
e mostre na tela cada um dos digitos separados
EX: 1834
Unidade: 4
Dezena: 3
Centena 8
Milhar: 1

dessa forma não funciona se não tiver os 4 digitos
'''

num = int(input('digite um numero: '))

n = str(num)

print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))