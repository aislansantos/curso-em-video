'''
Exercício Python 081:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

'''
# Importa biblioteca do sistema# Importa biblioteca do sistema
import os
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()
numeros = list()
cont = 0
while True:
    n = int(input('Digite um valor:'))
    numeros.append(n)
    cont += 1
    opcao = str(input('Desaja continuar[S/N] ?').strip().upper()[0:])
    if opcao == 'N':
        break
print(f'Você digitou {cont} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescentes são: {numeros}')
if 5 in numeros:
    print(f'Contém numero 5 na lista!')
else:
    print(f'Não contém o 5 na lista!')
print()
print('{:-^150}'.format(' FIM '))
print()
