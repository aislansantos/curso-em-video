'''
Exercício Python 039:
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import os #Importa biblioteca do sistema
from datetime import date
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('-='*25 + ' Alistamento Militar ' + '=-'*25)
print()

print('Sexo:')
print('1 - Feminino')
print('2 - Masculino')
sexo = int(input('Digite a opção do seu sexo: '))
print()
if sexo == 1:
    print('Você não precisa se alistar!')    
elif sexo == 2:
    ano = int(input('Em que ano você nasceu? '))
    hoje = date.today().year
    idade = hoje - ano

    print('Você tem {} anos em {}'.format(idade, hoje))
    if idade == 18:
        print('Pode se alistar')
    elif idade < 18:
        diferença = 18 - idade
        ano_alistamento = hoje + diferença
        print('Falta {} anos para se alistar'.format(diferença))
        print('Seu alistamento será em {}'.format(ano_alistamento))
    elif idade > 18:
        diferença = idade - 18
        ano_alistamento = hoje - diferença
        print('Você passou {} anos do prazo de alistamento!'.format(diferença))
        print('Seu alistamento foi em {}'.format(ano_alistamento))
else:
        print('Opção Inválida!')

print()
print('-='*25 + ' FIM' + '=-'*25)
print()
