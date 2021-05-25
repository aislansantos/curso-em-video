import os
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

for c in range(6, 0, -1):# Dessa forma ele conta de 6 a 0, faz regressiva tem de colocar o -1 para fazer a contagem da forma correta, 
    print(c)

print()

for c in range(0, 7, 2):# Depois da faixa de contador colocamos uma virgula e podemos especificar como o contador vai se portar
    print(c)

print()

#usamos uma variavel para colocarmos os passos a serem dados e até quanto contar
n = int(input('digite um número: '))
repeticoes = int(input('Digite até quanto contar: '))
for c in range(0, repeticoes + 1, n):
    print(c)

print('')

s= 0 
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # forma abreviada de fazer s = s + n
print('O somatório de todos os valores é de {}'.format(s))
