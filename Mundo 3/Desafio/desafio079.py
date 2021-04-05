'''
Exercício Python 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

'''
import os  # Importa biblioteca do sistema
# limpa a tela na inicialização do programa
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('{:-^150}'.format(' Exercicio '))
print()

numeros = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n in numeros:
        print('valor duplicado! Não vou adicionar')
    else:
        numeros.append(n)
    opcao = str(input('Deseja continuar?[S/N]').strip().upper())[0:]
    if opcao == 'N':
        break 
print(f'Você digitou o seguintes números: {sorted(numeros)}')
print()
print('{:-^150}'.format(' FIM '))
print()

