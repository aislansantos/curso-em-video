'''


'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

pessoa = dict()

print()
print('{:-^150}'.format(' Exercicio '))
print()


pessoa['nome'] = str(input('Nome: '))
ano = int(input('Nascimento: '))
pessoa['idade'] = 2021 - ano
pessoa['ctps'] = int(input('Carteira de Trabalho: '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = (pessoa['contratacao'] + 35) - ano

print('{:-^150}'.format(' Resultados '))

for k, v in pessoa.items():
    print(f'{k} tem o valor {v }')
print()
print('{:-^150}'.format(' FIM '))
print()