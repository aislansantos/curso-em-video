'''
Exercício Python 073:
Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Exercicio '))
print()

times = ('Corithians', 'Palmeiras', 'Santos', 'Gremio','Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(times)
print('{:-^150}'.format('TABELA BRASILEIRÃO 2017'))
for time in range(0, len(times)):
    print('{}º - {}'.format((time +1), times[time]))
print()

print('A - Os 5 primeiros times.')
print('Os 5 primeiros times são {}'.format(times[:5]))
print()
print('Os 5 primeros colocados são:')
for primeiros in range(0, 5):
    print('{}º - {}'.format((primeiros + 1),times[primeiros]))
print()

print('B - Os últimos 4 colocados.')
print('Os últimos 4 colocados são {}'.format(times[:-5:-1]))
print('{}'.format(times[16::]))
print()
print('Os últimos 4 colocados são:')
for ultimos in range(len(times)-1,15,-1):
    print('{}º - {} '.format((ultimos + 1), times[ultimos]))

print()
print('C - Os Times em ordem alfabética.')
print(sorted(times))
print()
nova = sorted(times)
for i in range(0, len(nova)):
    print(nova[i])
print()

print('D - Em que posição está o time da Chapecoense.')
print('A Chapecoense está na {}ª posição'.format(times.index('Chapecoense')+1))


print()
print('{:-^150}'.format(' FIM '))
print()
