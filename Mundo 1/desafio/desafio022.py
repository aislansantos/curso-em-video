'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

* O nome com todas as letras maiúsculas
* O nome com todas as letas minúsculas
* Quantas letras sem considerar espaços
* Quantas letras tem o primeiro nome
'''

nome = input('Digite um Nome: ')
print(nome)

print(nome.upper())
print(nome.lower())

#dividi o nome juntei sem espaço nenhum e mostrei e contem o nome sem espços
nome_dividido =  nome.split()
nome_junto = (''.join(nome_dividido))
print(len(nome_junto))

# peguei o nome dividido e ja mostrei quantas letras tem o primeiro nome
print(len(nome_dividido[0]))
