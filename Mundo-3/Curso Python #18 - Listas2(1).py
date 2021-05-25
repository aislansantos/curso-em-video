dados = list()
dados.append('pedro')
dados.append(25)
'''
print(dados)
print(dados[0])
print(dados[1])
'''

pessoa= list()
# o [:] é um fatiamento completo criando uma copia de dados dentro de pessoas
pessoa.append(dados)
print(pessoa)

pessoas = [['pedro', 25], ['maria', 19], ['joão', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])