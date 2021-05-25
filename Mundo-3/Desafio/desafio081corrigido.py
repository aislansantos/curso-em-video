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
while True:
    numeros.append(int(input('Digite um valor:')))
    opcao = str(input('Desaja continuar[S/N] ?').strip().upper())[0]
    # Usando o im na leitura para parar o programa
    if opcao in 'N':
        break
# Usando o len para mostrar a quantidade de numeros na lista
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescentes são: {numeros}')
if 5 in numeros:
    print(f'Contém numero 5 na lista!')
else:
    print(f'Não contém o 5 na lista!')
print()
print('{:-^150}'.format(' FIM '))
print()
