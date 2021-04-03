'''
Exercício Python 076:
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
import os  # Importa biblioteca do sistema
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()

produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.00,
            'Apontador do mikey', 5.50,
            'Pasta arquivos suspenso', 15)

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
print()
# tratando a tupla por posição(numero de index)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<40}', end=' ')
    elif i % 2 == 1:
        print(f'R$ {produtos[i]:>5.2f}')
print()
print('-'*50)

# tratando pelo tipo do dado string ou float/string
for i in range(0, len(produtos)):
    if type(produtos[i]) == str:
        print('{:.<40} R$'.format(produtos[i]), end=' ')
    else:
        print('{: >5.2f}'.format(produtos[i]))


print()
print('{:-^150}'.format(' FIM '))
print()
