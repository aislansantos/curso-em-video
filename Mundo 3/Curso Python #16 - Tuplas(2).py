import os
os.system('cls')
#arquivo criado para a a aula de tuplas mudando o tema do primeiro arquivo que era sobre a tupla lanche
a = (2, 5, 4)
b = (5, 8, 1, 2)
# a + b não a mesma coisa que b + a como no exemplo do resultado abaixo
c = a + b
d = b + a
print(c)
print(d)
print(len(c))
# a tupla tem alguns objetos de metodos internos como o COUNT Abaixo que no cado do exemplo mostra que o 5 apareceu 2 vezes
print(c.count(5))
# o medoto index que mostra qual a localização do item dentro da tupla nesse caso ele pega o indice da primeira ocorrencia como o caso
# do numero 2
print(d.index(2))
# Para pegar a ocorrencia do index depois de determinada posição fa\zemos da seguinte forma se chama deslocamento
print(d.index(2, 4))
# as tuplas pode conter dados de tipo diferentes como no exemplo abaixo
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
# A tupla não pode ser alterada, só que ela pode ser apagada
del(pessoa)
print(pessoa)