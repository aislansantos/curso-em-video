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

c = 0
while c == 0:
    sexo = str(input('Digite seu sexo[M/F]: ')).strip()
    if sexo in 'Mm' or sexo in'Ff':
        c = 1
        

print()
print('{:-^150}'.format(' FIM '))
print()