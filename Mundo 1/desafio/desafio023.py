'''
Faça um programa que leia um numero de 0 a 9999
e mostre na tela cada um dos digitos separados
EX: 1834
Unidade: 4
Dezena: 3
Centena 8
Milhar: 1
'''

n = input('leia um numero: ')

tamanho = (len(n))

if (tamanho == 1) :
    unidade = n[0]
    print('unidade: {}'.format(unidade))
elif (tamanho == 2) :
    unidade = n[1]
    dezena = n[0]
    print('unidade: {}'.format(unidade))
    print('Dezena: {}'.format(dezena))
elif (tamanho == 3) :
    unidade = n[2]
    dezena = n[1]
    centena = n[0]
    print('unidade: {}'.format(unidade))
    print('Dezena: {}'.format(dezena))
    print('Centena: {}'.format(centena))
elif (tamanho == 4):
    unidade = n[3]
    dezena = n[2]
    centena = n[1]
    milhar = n[0]
    print('unidade: {}'.format(unidade))
    print('Dezena: {}'.format(dezena))
    print('Centena: {}'.format(centena))
    print('Milhar: {}'.format(milhar))
else:
    print('numero fora do intervalo')