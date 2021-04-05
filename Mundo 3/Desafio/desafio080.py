'''
Exercício Python 080:
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

'''
import os  # Importa biblioteca do sistema
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()
numeros = list()
for i in range(0, 5):
    n = int(input('Digite um valor:'))
    if i == 0:
        numeros.append(n)
    elif n < min(numeros):
        numeros.insert(0, n)
        print('adicionado no inicio da lista')
    elif n >= max(numeros):
        numeros.append(n)
        print('Adicionado no final  da lista')
    elif n > min(numeros) and n < numeros[1]:
        numeros.insert(1, n)
        print(f'Adicionado na posição 1')
    elif n < max(numeros):
        numeros.insert(len(numeros)-1, n)
        print(f'Adicionado na posição {len(numeros)-2}')
print(numeros)
print()
print('{:-^150}'.format(' FIM '))
print()
