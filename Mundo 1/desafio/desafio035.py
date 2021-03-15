'''
Exercício Python 035: Desenvolva um programa que leia
o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa


print()
print('-='*25 + ' Existencia do Triangulo ' + '=-'*25)
print()

reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta:'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2: 
    print('Com essas medida a condição de existencia de um triângulo É VERDADEIRA')
else:
     print('Com essas medida a condição de existencia de um triângulo É FALSA')


print()
print('-='*25 + ' Selecionando Maior Número ' + '=-'*25)
print()
