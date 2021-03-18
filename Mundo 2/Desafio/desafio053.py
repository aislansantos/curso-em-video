'''
Exercício Python 053:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:=^150}'.format(' NÚMEROS PRIMOS '))
print()

frase = str(input('Digite uma frase: ')).strip().upper()
#tratamento de strings
palavras = frase.split()
frase_join = ''.join(palavras)
tamanho  = len

#mostrar 
print(frase_join)
print(palavras)
print(tamanho)

print()
print('{:=^150}'.format(' FIM '))
print()