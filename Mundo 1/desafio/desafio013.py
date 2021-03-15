# salario + 15% de aumento
salario = float(input('Salario do Funcionario: R$ '))
aumento = salario * 0.15

novo_salario = salario + aumento

print('O salario desse funcionario era de {:.2f}, seu aumento de 15 % é de {:.2f}, totalizando {:.2f}'.format(salario, aumento, novo_salario))