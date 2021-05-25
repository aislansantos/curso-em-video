'''
Exercício Python 085:
Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.

'''
import os  # Importa biblioteca do sistema
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()

numeros = [[], []]
valores = 0
for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}º numero: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 == 1:
        numeros[1].append(valor)

numeros.sort()

print('-=' * 30)
print(f'Os valore pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')

print()
print('{:-^150}'.format(' FIM '))
print()
