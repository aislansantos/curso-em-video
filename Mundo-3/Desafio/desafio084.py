'''
Exercício Python 084:
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

'''
import os  # Importa biblioteca do sistema
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()

lista = list()
dados = list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    opcao = (str(input('Deseja Continuar ?'))).strip()[0]
    if opcao in 'Nn':
        break
print('-==-' * 15)
print(f'Ao todo você cadastrou {len(lista)} pessoas')
for pos, peso in enumerate(lista):
    if pos == 0:
        pesado = leve = peso[1]
    else:
        if pesado < peso[1]:
            pesado = peso[1]
        if leve > peso[1]:
            leve = peso[1]
print(f'Os mais pesadoos com {pesado} Kg, são: ', end='')
for p in lista:
    if p[1] == pesado:
        print(f'{p[0]} ', end='')
print(f'\nOs mais leves com {leve} kg são: ', end='')
for l in lista:
    if l[1] == leve:
        print(f'{l[0]} ', end='')
print()
print(lista)
print('{:-^150}'.format(' FIM '))
print()
