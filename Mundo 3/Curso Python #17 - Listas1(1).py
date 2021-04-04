import os
os.system('cls')

# Diferentes das tuplas as listas são MUTÁVEIS, mostrando abaixo na lista que pode ser alterado um elemento da lista

# declaração de Lista
lanche = ['haburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
print(lanche)

# A lsta também pode receber um novo item, usando metodo append - adiciona um elemento no final da lista
lanche.append('cookie')
print(lanche)

# Pode se adicionar um item extra em outro ponto da lista usando o metodo insert - indica-se onde se quer o novo elemento
lanche.insert(0, 'cachorro quente')
print(lanche)

# Para apgar elementos da lista usa-se 2 comandos:
# O comando mais básico é o del - por indice
#del lanche[3]
# print(lanche)
# Tem também o método pop - normalmente usa-se o pop para elimitar o ultimo elemento, porém pode se passar o indice para excluir determinado elemento
lanche.pop()
print(lanche)
# Temos também o método remove - nesse caso se indica o item pelo nome não pelo indice . ele procura do inicio da lista a primeira ocorrencia e exclui a mesma
# lanche.remove('pizza')
# print(lanche)
# Para não haver erro antes de remover temos de verificar se existe o que desejamos que seja removido usando if
if 'pizza' in lanche:
    lanche.remove('pizza')
    print('pizza removida')
else:
    print('Pizza não existe na lista')
print(lanche)

print()
# Podemos criar lista pela estrutura RANGE - no exemplo ele vai de 4 a 10(descarta-se o ultimo elemento) pulando de 2 em 2
valores = list(range(4, 11, 2))
print(valores)

print()
# Para ordenar as listas podemos fazer de maneira simples ultilizando o método sort
valores_novos = [8, 2, 5, 4, 9, 3, 0]
valores_novos.sort()
print(valores_novos)
# Para ordenar do final para o iinicio ultiza-se o parametro reverse dentro do sorte
valores_novos.sort(reverse=True)
print(valores_novos)

# para saber o tamnho de uma lista podemos usar a função len do Python
print()
print(len(lanche))
print(len(valores))
print(len(valores_novos))
