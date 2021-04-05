'''
Exercício Python 083:
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os
 parênteses abertos e fechados na ordem correta.

'''
# Importa biblioteca do sistema
import os
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')
print()
print('{:-^150}'.format(' Exercicio '))
print()
expr = str(input('Digite uma expressão: ')).strip()
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
print()
print('{:-^150}'.format(' FIM '))
print()
