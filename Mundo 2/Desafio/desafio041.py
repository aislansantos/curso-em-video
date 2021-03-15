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
from datetime import date

print()
print('-='*25 + ' Classificação de Atletas' + '=-'*25)
print()

ano_nascimento = int(input('Digite o ano de nascimento do Atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Esse atleta tem {} anos, ele é MIRIM'.format(idade))
elif idade <= 14:
    print('Esse atleta tem {} anos, ele é INFANTIL'.format(idade))
elif idade <= 19:
    print('Esse atleta tem {} anos, ele é JÚNIOR'.format(idade))
elif idade <= 25:
    print('Esse atleta tem {} anos, ele é SÊNIOR'.format(idade))
else:
    print('Esse atleta tem {} anos, ele é MASTER'.format(idade))

print()
print('-='*25 + ' FIM' + '=-'*25)
print()
