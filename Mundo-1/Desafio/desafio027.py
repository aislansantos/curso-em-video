'''
Faça um programa que que leia um nome completo mostrando em seguida
o primeiro e o ultimo nome separadamente

EX: Ana Maria de Souza
Primeiro: Ana
Ultimo: Souza
'''

nome = str(input('Digite um nome: ')).strip()
nome_fatiado = nome.split()


primeiro_nome = nome_fatiado[0]
ultimo_nome = nome_fatiado[-1]

print('Primeiro nome é: {}'.format(primeiro_nome))
print('Primeiro nome é: {}'.format(ultimo_nome))