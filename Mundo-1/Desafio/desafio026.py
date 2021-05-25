'''
Faça um programa que leia uma frase e mostre:

* Quantas vezes aparece a letra "A".

* Em que posição ela aparece pela primeira vez.

* Em que posição ela aparece pela última vez.
'''

frase = str(input('Digite uma frase: ')).lower().strip()
letra = frase.count('a')
primeiro_a = frase.find('a') + 1
ultimo_a = frase.rfind('a') + 1
print(len(frase))
print('Sua frase tem {} letras "A"'.format(letra))
print('Sua primeira letra "A" está na posição {}'.format(primeiro_a))
print('Sua última letra "A" está na posição {}'.format(ultimo_a))
