'''
Exercício Python 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
import os #Importa biblioteca do sistema
os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela na inicialização do programa

print()
print('-='*25 + ' IMC ' + '=-'*25)
print()

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua Altura: '))
imc = peso / (altura * altura)


if imc < 18.5:
    print('Abaixo do Peso, seu IMC é: {:.1f}, está abaixo do recomendado que é acima de 18.5'.format(imc))
elif imc <= 25:
    print('Peso Ideal, seu IMC é: {:.1f}'.format(imc))
elif imc < 30:
     print('Sobrepeso, seu IMC é: {:.1f}, está acima do recomendado que é entre 18.5 e 25'.format(imc))
elif imc < 40:
     print('Obesidade, seu IMC é: {:.1f}, está acima do recomendado que é entre 18.5 e 25'.format(imc))
else:
    print('Obesidade Mórbida, seu IMC é: {:.1f}, está MUITO acima do recomendado que é entre 18.5 e 25, procure ajuda. risco de saude !'.format(imc))
    

print()
print('-='*25 + ' FIM' + '=-'*25)
print()
