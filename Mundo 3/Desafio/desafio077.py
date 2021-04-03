'''
Exercício Python 077:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

palavras = ('casa', 'terreno', 'contrução', 'projeto', 'pedreiro', 'cimento', 'loja', 'tempo', 'programação')

print(palavras)

contador = 0
while True:
    if contador == len(palavras):
        break
    print(f'{palavras[contador]} tem as seguintes vogais', end=' ')
    for i in palavras[contador]:
        if 'a' in i:
            print(i, end=' ')
        elif 'e' in i:
            print(i, end=' ')
        elif 'i' in i:
            print(i, end=' ')
        elif 'o' in i:
            print(i, end=' ')
        elif 'u' in i:
            print(i, end=' ')
    contador += 1
    print()
print()
print('{:-^150}'.format(' FIM '))
print()

