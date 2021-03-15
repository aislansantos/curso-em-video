'''
Crie um programa que leia o nome da pessoa e diga se ela tem
"SILVA" no nome
'''

nome = input('Digite seu nome: ').strip()
silva = ('silva' in nome.lower())
print('Seu nome tem "SILVA"? {}'.format(silva))