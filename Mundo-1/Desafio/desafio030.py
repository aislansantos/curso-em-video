'''
Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
print()
print('='*45 + ' PAR OU IMPAR ' + '='*45)
print()

n = int(input('Digite um Número: '))
div = n%2
if div == 0:
    print('Número PAR')
else:
    print('Número IMPAR')

print()
print ('='*50 + ' FIM ' + '='*50)