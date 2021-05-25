'''
Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('-='*25 + ' Cálculo de Média ' + '=-'*25)
print()

cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'vermelho':'\033[31m',
         'alerta': '\033[35m'
         }

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))

if nota1 < 0 or nota1 > 10:
    print('1ª nota, só é permitido valores de {}0 a 10{} e você digitou {:.2f}.'.format(cores['alerta'], cores['limpa'], nota1))
elif nota2 < 0 or nota2 > 10:
       print('2ª nota, só é permitido valores de {}0 a 10{} e você digitou {:.2f}.'.format(cores['alerta'],cores['limpa'],  nota1))
else:
    media = (nota1 + nota2) / 2
    if media < 5:
        print('sua média foi {} {:.2f} {}, você foi reprovado!'.format(cores['vermelho'], media, cores['limpa']))
    elif media >= 5 and media < 7:
        print('sua média é {} {:.2f} {}, você está de recuperação!'.format(cores['amarelo'], media, cores['limpa']))
    elif media >= 7:
        print('Sua média foi {} {:.2f} {}, parabéns voce foi APROVADO!'.format(cores['verde'], media, cores['limpa']))

print()
print('-='*25 + ' FIM' + '=-'*25)
print()
