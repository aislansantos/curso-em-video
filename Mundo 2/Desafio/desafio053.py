'''
Exercício Python 053:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:=^150}'.format(' NÚMEROS PRIMOS '))
print()

frase = str(input('Digite uma frase: ')).strip().upper()
#tratamento de strings
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#exercicio feito inverso por fatiamento sem for
inverso = junto[::-1]

#exercicio feito inverso por for
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
'''
print('o inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('palindrono')
else:
    print('não é palindrono')

print()
print('{:=^150}'.format(' FIM '))
print()