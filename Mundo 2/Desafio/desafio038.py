'''
Exercício Python 038:
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('-='*25 + ' Comparando Números ' + '=-'*25)
print()


n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um valor: '))

if n1 > n2:
    print('O primeiro valor é maior!')
elif n1 < n2:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')


print()
print('-='*25 + ' FIM' + '=-'*25)
print()
