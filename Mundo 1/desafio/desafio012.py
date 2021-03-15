# ler preço e mostrar com 5 % de desconto
valor = float(input('Digite o valor do produto: R$ '))
desc = valor * 0.05
desconto = valor - desc

print('O valor do produto é de R$ {:.2f}, com o desconto de 5% sai por R$ {:.2f} - total do desconto é de R$ {:.2f}'.format(valor, desconto, desc))