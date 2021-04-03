'''
Exercício Python 072:
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

numero = (
    'zero', 'hum', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezesete', 'dezoito',
    'dezenove', 'vinte'
)
while True:
    while True:
        selecionado = int(input('Digite um valor de 0 a 20: '))
        if selecionado >= 0 and selecionado <= 20:
            break
        print('tente novemente.', end=' ')
    print(f'Você digitou o número {numero[selecionado]}')
    opcao = str(input('Desesa continuar[S/N] ?')).strip().upper()
    if opcao == 'N':
        break
        
print()
print('{:-^150}'.format(' FIM '))
print()
