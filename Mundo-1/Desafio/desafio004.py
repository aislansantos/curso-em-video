# Faça um programa que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('digite alguma coisa: ')
print(n)
print('o tipo primitivo desse valor é: {}'.format(type(n)))
print('o que foi digitado é número: {}'.format(n.isalnum()))
print('o que foi digitado é letra ?', n.isalpha())
print('o que foi digitado é alfa-númerico ?', n.isalnum())
print('o que foi digitado é somente espaço ?', n.isspace())
print('o que foi digitado está mauiscula ?', n.isupper())
print('o que foi digitado está minusculo ?', n.islower())