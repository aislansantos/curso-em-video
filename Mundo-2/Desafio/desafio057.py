'''
Exercício Python 057:
Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()
sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0] # o [0] é fatiamento pegando só a primeira letra da  palavra

while sexo not in 'MF':
    sexo = str(input('Dados invalidos, informe seu sexo[M/F]: ')).strip().upper()[0] # o [0] é fatiamento pegando só a primeira letra da  palavra
print('Sexo {} digitado com sucesso'.format(sexo))

print()
print('{:-^150}'.format(' FIM '))
print()