'''
Exercício Python 034: Escreva um programa
que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
print()
print('-='*25 + ' Calculo Aumento Salárial ' + '=-'*25)
print()



salario = float(input('Digite seu salário: R$ '))

if (salario <= 1250):
    novo = salario + ((salario * 15) / 100 )
else:
    novo = salario + ((salario * 10) / 100)
print('Seu novo salário é de R$ {:.2f}'.format(novo))

print()
print ('-='*30 + ' FIM ' + '=-'*30)