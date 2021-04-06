'''
# Inserindo os dados dentro de uma alocação de memoria de pessoas conforme imagem (lista pessoas.png)
dados = list()
dados.append('pedro')
dados.append(25)
pessoas = list()
pessoas.append(dados[:])
print(pessoas)
'''

pessoas2 = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas2[0][0])
print(pessoas2[1][1])
print(pessoas2[2][0])
print(pessoas2[1])