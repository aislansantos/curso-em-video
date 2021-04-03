'''
Exercício Python 075:
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
import os  # Importa biblioteca do sistema
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()
# Entrada dos dados em Tupla
n = (int(input('Digite um numero: ')),
     int(input('digite um numero: ')),
     int(input('digite um numero: ')),
     int(input('digite um numero: ')))

print(f'Os numeros digitados foram: {n}')

par = 0

# função conta quantos numero 9 foram digitados
print(f'O valor 9 apareceu {n.count(9)} vezes')

# função que mostra em que posição da tupla o 3 foi digitado pela 1ª vez
if 3 in n:
    print(f'o numero 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado!')

# Ultima parte conta conta os numeros pares para saber se processa e em qual condição vai entrar
for x in range(0, len(n)):
    if n[x] % 2 == 0:
        par += 1

# Mostra o numero se foi somente 1 numero par digitado
if par == 1:
    print('o numero par digitado foi: ', end='')
    for x in range(0, len(n)):
        if n[x] % 2 == 0:
            print(f'{n[x]}', end='')
    print('.')
# Mostra os números pares que foram digitados se foi mais que 1
elif par > 1:
    print('os numero pares digitados foram: ', end='')
    for x in range(0, len(n)):
        if n[x] % 2 == 0:
            print(f'{n[x]} ', end='')
    print('.')


print()
print('{:-^150}'.format(' FIM '))
print()
