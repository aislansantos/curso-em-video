#as tuplas são IMUTAVEIS
#não pode se alterar os itens das tuplas
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
#print(lanche)
'''

for c in lanche:
    print(f'-> {c}')

print()

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print()
'''
print(len(lanche))

# O exemplo abaixo é bom para quando se pprecisa mostrar a posição ou fazer um menu
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print()
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')

# Método sorted, coloca em ordem os itens da tulpa, não muda a tupla só ordena na impressão
print(sorted(lanche))