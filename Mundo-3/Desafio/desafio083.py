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
expressao = []
e = str(input('Digite uma expressão: ')).strip()
for item in range(0, len(e)):
    expressao.append(e[item])
if expressao.count('(') == expressao.count(')'):
    print('Expressão está valida!')
else:
    print('Expressão está errada!')
print()
print('{:-^150}'.format(' FIM '))
print()
