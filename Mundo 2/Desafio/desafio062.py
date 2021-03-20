
'''
Exercício Python 062:
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

contador = 1
pa = termo

while contador != 0:
    contador = int(input('Dejesa mostrar mais quantos termos: '))
    for contagem in range(termo, contador + 1):
        print('{} -> '.format(pa),end='')
        pa += razão
    print('ACABOU')
        


print()
print('{:-^150}'.format(' FIM '))
print()
