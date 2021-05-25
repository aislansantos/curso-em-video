'''
Exercício Python 037:
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal
3 para hexadecimal.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('-='*25 + ' Base Numérica ' + '=-'*25)
print()

numero = int(input('Digite um numero: '))

print()
print('Opções:')
print('1 - Binario')
print('2 - Octal')
print('3 - Hexadecimal')
opcao =int(input('Escolha para qual sistema deseja converter esse numero: '))

if opcao == 1:
    #Código de conversão retirado da internet
    binario =(bin(numero)[2:])
    print('Binário: {}'.format(binario))
elif opcao == 2:
    #Código de conversão retirado da internet
    octal =(oct(numero)[2:])
    print('Octal: {}'.format(octal))
elif opcao == 3:
    #Código de conversão retirado da internet
    hexadecimal =(hex(numero)[2:])
    print('Hexadecimal: {}'.format(hexadecimal))
else:
    print('Opção Inválida!')

print()
print('-='*25 + ' FIM' + '=-'*25)
print()
