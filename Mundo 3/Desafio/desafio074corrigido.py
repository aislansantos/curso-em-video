'''
Exercício Python 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
import os  # Importa biblioteca do sistema
from random import randint
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()
x = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end=' ')
for n in x:
    print(f'{n}', end=' ')
# \n pula linha
print(f'\nO maior valor sorteado foi {max(x)}')
print(f'O menor valor sorteado foi {min(x)}')
print()
print('{:-^150}'.format(' FIM '))
print()
