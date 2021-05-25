
# Comando break en while infinito

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
# Atualização da forma de printar frases na tela, da PEP498 CHAMADA FSTRINGS

# FORMA ANTIGA(todos os exemplos e desafios até hoje)
# print('a soma dos numeros = {}'.format((s)))

# FORMA NOVA FSTRINGS
print(f'a soma vale {s}')


nome = 'José'
idade = 33
salario = 987
print(f'O {nome:-^20} tem {idade} anos e ganha R$ {salario:.2f}')