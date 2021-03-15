'''
Exercício Python 029: Escreva um programa que leia
a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
print()
print('-='*26 + ' Calculo de multa ' + '=-'*26)
print()

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade >= 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print('Voce ultrapassou o limite de velocidade, estava a {} Km/h, {} Km/h acima do limite, sua Multa é de R$ {:.2f}'.format(velocidade, excesso,multa))
else:
    print('Bom dia, pode seguir seu caminho!')

print()
print ('-='*30+ ' FIM ' + '-='*30)