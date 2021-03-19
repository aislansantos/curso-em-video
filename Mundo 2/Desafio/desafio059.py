'''
Exercício Python 059:
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro numero: '))
print('{:-^150}'.format(' Opções '))


status = 0

while status < 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Numeros')
    print('[ 5 ] Sair do Programa')
    status = int(input('Digite sua opção: '))

    if status == 1:
        print()
        print('A soma de {} e {} = {}'.format(n1, n2, n1 + n2))
        print()
        print('{:-^150}'.format(' Opções '))
    if status == 2:
        print()
        print('A multiplicação de {} * {} = {}'.format(n1, n2, n1 * n2))
        print()
        print('{:-^150}'.format(' Opções '))
    if status == 3:
        if n1 > n2:
            print()
            print('Entre {} e {} o maior numero é {}'.format(n1, n2, n1))
            print()
            print('{:-^150}'.format(' Opções '))
        else:
            print()
            print('Entre {} e {} o maior numero é {}'.format(n1, n2, n2))
            print()
            print('{:-^150}'.format(' Opções '))
    if status == 4:
        print('{:-^150}'.format(' Nova Entrada de Valores '))
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro numero: '))
        print('{:-^150}'.format(' Opções '))
    
    
    
        
            
        

print()
print('{:-^150}'.format(' FIM '))
print()
