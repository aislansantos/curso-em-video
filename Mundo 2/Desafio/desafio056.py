'''
Exercício Python 056:
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

total_idade  = 0
mais_velho = 0
nome_velho = ''
mulheres_novas = 0
for pessoa in range(1, 5):
    print()
    print('{:-^150}'.format('{}ª PESSOA'.format(pessoa)))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:[M/F] ')).strip().upper()
    total_idade += idade
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            if idade > mais_velho:
                mais_velho = idade
                nome_velho = nome
        if sexo == 'F':
            if idade < 20:
                mulheres_novas += 1
    else:
        print('uma opção inválida')   
print()   
print('{:-^150}'.format('Saida de dados'))
media = total_idade / pessoa
print('A média de idade de todas as {} pessoas, é de {} anos'.format(pessoa,media))
if mais_velho > 0:
    print("O homem mais velho é o {}, ele tem {} anos".format(nome_velho, mais_velho))
if mulheres_novas > 1:   
    print('Existem {} mulheres com idade abaixo dos 20 anos'.format(mulheres_novas))
else:
    print('Existe {} mulher com idade abaixo dos 20 anos'.format(mulheres_novas))
print()
print('{:-^150}'.format(' FIM '))
print()
