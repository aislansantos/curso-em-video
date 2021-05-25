
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
razao = int(input('Digite a razão: '))

controle = 0
pa = termo
mais = 10
total = 0

while mais != 0:
    total += mais
    while controle < total:
        print('{} -> '.format(pa), end='' )
        pa += razao
        controle += 1
    print('Pausa')
    mais = int(input('Quantos termos mostrar: '))
print('ACABOU com {} termos mostrados!'.format(controle))
    
        


print()
print('{:-^150}'.format(' FIM '))
print()
