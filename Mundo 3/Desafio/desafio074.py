'''
Exercício Python 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
import os #Importa biblioteca do sistema
from random import randint
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()


x = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: {x}')
if x[0] >= x[1] and x[0] >= x[2] and x[0] >= x[3] and x[0] >=  x[4]:
    print(f'o maior numero é  {x[0]} ')
elif x[1] >= x[0] and x[1] >= x[2] and x[1] >= x[3] and x[1] >=  x[4]:
    print(f'o maior numero é  {x[1]} ')
elif x[2] >= x[0] and x[2] >= x[1] and x[2] >= x[3] and x[2] >=  x[4]:
    print(f'o maior numero é  {x[2]} ')
elif x[3] >= x[0] and x[3] >= x[1] and x[3] >= x[2] and x[3] >=  x[4]:
    print(f'O maior numero é  {x[3]} ')  
elif x[4] >= x[0] and x[4] >= x[1] and x[4] >= x[2] and x[4] >=  x[3]:
    print(f'O maior numero é  {x[4]} ')

if x[0] <= x[1] and x[0] <= x[2] and x[0] <= x[3] and x[0] <=  x[4]:
    print(f'o menor numero é  {x[0]} ')
elif x[1] <= x[0] and x[1] <= x[2] and x[1] <= x[3] and x[1] <=  x[4]:
    print(f'o menor numero é  {x[1]} ')
elif x[2] <= x[0] and x[2] <= x[1] and x[2] <= x[3] and x[2] <=  x[4]:
    print(f'o menor numero é  {x[2]} ')
elif x[3] <= x[0] and x[3] <= x[1] and x[3] <= x[2] and x[3] <=  x[4]:
    print(f'O menor numero é  {x[3]} ')  
elif x[4] <= x[0] and x[4] <= x[1] and x[4] <= x[2] and x[4] <=  x[3]:
    print(f'O menor numero é  {x[4]} ')






print()
print('{:-^150}'.format(' FIM '))
print()
