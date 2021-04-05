'''
Exercício Python 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''
import os  # Importa biblioteca do sistema
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio 78 lista '))
print()
numeros = list()
for num in range(0, 5):
    numeros.append(int(input(f'Digite um valor na posição {num}: ')))
print(f'Você digitou os valores: {numeros}')
maior = max(numeros)
menor = min(numeros)
print(f'O maio valor digitado foi {maior} e está nas posições ', end='')
for posicao in range(0, len(numeros)):
    if numeros[posicao] == maior:
        print(f'{posicao}...', end='')
print(f'\nO menor valor digitado foi {menor} e está nas posições ', end='')
for posicao in range(0, len(numeros)):
    if numeros[posicao] == menor:
        print(f'{posicao}... ', end='')
print()
print('{:-^150}'.format(' FIM '))
print()
