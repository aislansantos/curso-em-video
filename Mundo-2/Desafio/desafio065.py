'''
Exercício Python 065:
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

opcao = ''
total = contador = maior = menor = 0

while opcao != 'n':
    n = int(input('Digite um numero: '))
    if contador == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    total += n   
    contador += 1
    opcao = str(input('Deseja continuar ?[s/n]'))

media = total / contador
print('A média dos numeros foi {}'.format(media))
print('O maior numero digitado foi {}'.format(maior))
print('O menor numero digitado foi {}'.format(menor))

print()
print('{:-^150}'.format(' FIM '))
print()
