'''


'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Desafio Dicionarios 1 '))
print()

aluno = dict()

aluno['Nome'] = str(input('Nome: '))
print(f'Média de {aluno["Nome"]}: ', end='')

aluno['Média'] = float(input())

if aluno['Média'] <= 5:
    aluno['Situação'] = 'Reprovado'
if aluno['Média'] <= 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovardo'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

print()
print('{:-^150}'.format(' FIM '))
print()

