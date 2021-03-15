n1 = int(input('Um Valor: '))
n2 = int(input('OUtro Valor: '))
s = n1 + n2
m = n1 * n2
sub = n1 - n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# quebra de linha \n - quando tudo esta dentro de um print só
# quando se tem mais de 2 prints e não se quer quebrar a linhda usamos no final de tudo end=''
print('a soma é {}, \n a multiplicação é {}, a subtração é {}, a divisão é {:.3f}, a divisão inteira é {}, e a exponenciação é {}'.format(s,m,sub,d,di,e))