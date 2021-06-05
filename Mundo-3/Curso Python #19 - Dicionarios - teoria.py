# abaixo as duas formas de iniciar uma Dicionario
dados = dict()
dados = {}

dados = {'nome': 'pedro', 'idade': 25}

dados['sexo'] = 'M'
del dados['idade']
print(dados)

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'Geoge Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
print()
print('='*150)
print('')
for k, v in filme.items():
    print(f'{k} é {v}')

print('='*150)
print('podemos usar dicionario e listas juntos como no exmplo abaixo')

locadora = []
locadora.append(filme)
print (locadora[0]['ano'])
