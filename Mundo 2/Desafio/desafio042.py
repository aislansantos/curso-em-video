'''
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('-='*25 + ' Tipos de Triangulos' + '=-'*25)
print()

reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta:'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2: 
    if reta1 == reta2 and reta2 == reta3:
        print('Com essas medida a condição de existencia de um triângulo É VERDADEIRA, esse é um triangulo EQUILATERO!')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('Com essas medida a condição de existencia de um triângulo É VERDADEIRA, esse é um triangulo ISOCELES')
    else:
        print('Com essas medida a condição de existencia de um triângulo É VERDADEIRA, esse é um triangulo ESCALENO')
else:
     print('Com essas medida a condição de existencia de um triângulo É FALSA')

print()
print('-='*25 + ' FIM' + '=-'*25)
print()
