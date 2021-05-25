'''
Exercício Python 049:
Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' TABUADA '))
print()

tabuada = int(input('Digite de qual tabuada vc quer: '))
for c in range(1, 11):
    print('{} * {:2} = {}'.format(tabuada, c, tabuada*c))

print()
print('{:-^150}'.format(' FIM '))
print()
