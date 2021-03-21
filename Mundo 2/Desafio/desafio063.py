'''
Exercício Python 063:
Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

n = int(input('Digite seu quantos termos você quer mostrar:'))

''' no caso da sequencia de Fibonacci, temos o t1 e o t2 como "fixos", na verdade precisamos dessas duas variaveis
    para conseguirmo fazer o processo necessário dentro do while'''
t1 = 0 # Primeiro termo da sequencia
t2 = 1 # Segundo termo da sequencia
contador = 3 # O contador vai começar a partir do 3º termo pq ja temos os outros temos acima

print('{} -> {}'.format(t1, t2), end='') # tendo os termos ja podemos imprimi-los na tela

while contador <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    ''' Abaixo fazemos as trocas de valores de lugares para conseguir fazer a som e mostrar o t3 evoluindo na progressão 
        a prtir do momento que atribuimos o t1 = t2 e t2 = t3 deixamos o t3 livre para o novo calculo com as variaveis 
        ja atualizadas nas questão dos valores para a soma'''
    t1 = t2
    t2 = t3    
    contador += 1

print()
print('{:-^150}'.format(' FIM '))
print()
