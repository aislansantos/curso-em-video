#algoritmo que mostre o numero o dobro, triplo e raiz quadrada
n = int(input('Difgite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('Numero digitado:'.format(n))
print('O dobro de {} é {}'.format(n, d))
print('O triplo de {} é {}'.format(n,t))
print('A raiz quadrada de {} é {:.2f}'.format(n,r))