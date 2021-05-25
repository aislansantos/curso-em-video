import random
aluno1 = input('Digite um nome: ')
aluno2 = input('Digite um nome: ')
aluno3 = input('Digite um nome: ')
aluno4 = input('Digite um nome: ')
lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista)

print(escolhido)