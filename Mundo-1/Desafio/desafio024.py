'''
Crie um programa que leia o nome de uma cidade
e diga se o nome dela começa ou não com o nome
'SANTO'
'''
cidade = str(input('Digite o nome da cidade: '))
cidade = cidade.lower().strip()
n1 = cidade.split()
print('santo' in n1[0])