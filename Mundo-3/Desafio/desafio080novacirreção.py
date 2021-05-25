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
lista = list()

for i in range(0, 5):
    n = int(input('Digite um valor:'))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('adicionado no final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            print(pos, len(lista))
            print(n, lista[pos])
            if n < lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print(lista)
print()
print('{:-^150}'.format(' FIM '))
print()
