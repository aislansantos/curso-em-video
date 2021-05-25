'''
teste = list()
teste.append('Aislan')
teste.append(35)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem tantos {p[1]} anos de idade')]
'''
galera = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1]>= 21:
        print(f'{p[0]} é maior de idade!')