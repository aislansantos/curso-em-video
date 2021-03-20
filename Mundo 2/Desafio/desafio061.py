'''
Exercício Python 061:
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^70}'.format(' Exercicio '))
print()

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 1
pa = termo

while contador <= 10:
    print('{} ->'.format(pa), end='' )
    pa += razao
    contador += 1
print('ACABOU !')

print()
print('{:-^70}'.format(' FIM '))
print()