'''
Exercício Python 069:
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
import os  # Importa biblioteca do sistema
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()

pessoas_acima_18 = homens = mulheres = 0


while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    if idade > 18:
        pessoas_acima_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar ?')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'''Foram cadastradas {pessoas_acima_18} pessoas com mais de 18 anos.
Foram cadastrados {homens} homens.
Foram Cadastradas {mulheres} mulheres com menos de 20 anos.''')

print()
print('{:-^150}'.format(' FIM '))
print()
