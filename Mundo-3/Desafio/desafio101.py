'''


'''
import os  # Importa biblioteca do sistema
from datetime import date

os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela na inicialização do programa

print()
print('{:-^150}'.format(' Desafio Voto '))
print()


def voto(ano):
    # importado a biblioteca dentro da função pra economizar processamento
    from datetime import date
    atual = date.today().year
    anos = atual - ano
    if anos < 16:
        obg = 'Não vota!'
    elif 16 <= anos < 18 or anos > 65:
        obg = 'Voto Opicional!'
    else:
        obg = 'Voto Obrigatório!'
    print(f'Com {anos} anos: {obg} ')


ano = int(input('Em que ano você nasceu: '))
voto(ano)

print()
print('{:-^150}'.format(' FIM '))
print()
