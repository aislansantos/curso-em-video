# Mostrando como se formata a lista para mostrar de forma mais organizada
# Pode se criar uma lista vazia assim:
#valores = list()
# Ou pode se criar uma lista vazia assim:
'''
valores = []
valores.append(5)
valores. append(9)
valores.append(4)

print(valores)

for chave, valor in enumerate(valores):
    print(f'na posição {chave} encontrei o valor {valor} !')
print(f'Cheguei ao final da lista')

valores_digitados = list()
for cont in range(0, 5):
    valores_digitados.append(int(input('Digite um valor: ')))
print(valores_digitados)
print()
print()
'''
print('Isso é uma peculiaridade do Python')
# Feita uma ligação naão cópia no caso abaixo
# Quando duas listas são igauladas se mudar um item na lista filho a lista pai também altera pois são equivalentes
# Como no exmploe abaixo que alteramos a lista b como  a lista a foi igualada o python altera o item nas duas
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Para fazer uma cópia fazemos da forma Abaixo
# Lista C está recebendo uma cópia dos valores de A, isso que significa o código abaixo, trabalhando com fatiamento
c = a[:]
c[2] = 5
print(f'Lista A: {a}')
print(f'Lista C: {c}')
