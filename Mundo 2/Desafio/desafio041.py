'''
Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('-='*25 + ' Classificação de Atletas' + '=-'*25)
print()

idade = int(input('Digite a idade do Atleta: '))

if idade <= 9:
    print('Esse atleta é MIRIM')
elif idade <= 14:
    print('Esse atleta é INFANTIL')
elif idade <= 19:
    print('Esse atleta é JÚNIOR')
elif idade <= 25:
    print('Esse atleta é SÊNIOR')
else:
    print('Esse atleta é MASTER')

print()
print('-='*25 + ' FIM' + '=-'*25)
print()
