from math import sqrt, floor
import emoji
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num,floor(raiz)))

print(emoji.emojize("Ola mundo :earth_africa:", use_aliases=True))