'''
Exercício Python 054:
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
import os  # Importa biblioteca do sistema
from datetime import date
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()
atual = date.today().year
maiores = 0
menores = 0
for pessoa in range(1, 8):
    nascimento = int(
        input('Digite o ano do nascimento da {}ª pessoa: '.format(pessoa)))
    idade = atual - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('A quantidade de maiores é {}'.format(maiores))
print('A quantidade de menores é {}'.format(menores))

print()
print('{:-^150}'.format(' FIM '))
print()
