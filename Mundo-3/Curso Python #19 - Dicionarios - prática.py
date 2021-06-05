pessoas = {'nome': 'Aislan', 'sexo': 'M', 'idade': 36}
pessoas['peso'] = 95.8
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos ')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

# a função abaixo é como o enumarate nas tuplas e nas listas
for k in pessoas.keys():
    print(k)
print('+'*50)
for v in pessoas.values():
    print(v)
print('+'*50)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('+'*50)

