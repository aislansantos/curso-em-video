'''
Exercício Python 031: Desenvolva um programa que pergunte a
distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
parta viagens mais longas.
'''
print()
print('='*45 + ' Calculo de Passagem ' + '='*45)
print()


distancia = float(input('Digite a distancia da viagem: '))

if distancia <= 200:
    valor_viagem = distancia * 0.50
else:
    valor_viagem = distancia * 0.45
print('Valor total da passagem é de R$ {:.2f}'.format(valor_viagem))


print()
print ('='*50 + ' FIM ' + '='*50)