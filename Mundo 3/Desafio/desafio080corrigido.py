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
# Otimizado com while para melhorar o codigo na correção
for i in range(0, 5):
    n = int(input('Digite um valor:'))
    if i == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado a posição {pos}')
                break
            pos += 1
print('-=-' * 15)
print(f'Os valores digitador em ordem foram {numeros}')
print()
print('{:-^150}'.format(' FIM '))
print()
