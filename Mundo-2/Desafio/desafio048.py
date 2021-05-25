'''
Exercício Python 048:
Faça um programa que calcule a soma entre todos os números
 que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' SOMA '))
print()

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
            

print('A somatória de todos os numeros impares multiplos de 3 de 1 a 500 é {} no total de {} numeros que atende ao que foi pedido!'.format(soma, contador))
print()
print('{:-^150}'.format(' FIM '))
print()
