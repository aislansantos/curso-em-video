print('=' * 10 + ' Exemplos Práticos Condicional IF ' + '=' * 10)

# primeiro exemplo
nome = str(input('Qual é seu nome? ')).capitalize().strip()
if nome == 'Aislan':
    print('Que nominho heim?')
else:
    print('Seu nome é normal!')
print('bom dia, {}!!!'.format(nome))


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!') 