nome = str(input('Qual é o seu nome ?')).strip()
if nome == "Aislan":
    print('Que nome bonito {}'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil, {}!'.format(nome))
elif nome in 'Juca Josefa Carlotina':
    print('Etâ nome diferente, {}!'.format(nome))
else:
    print('Seu nome é normal {}'.format(nome))
print('Tenha um bom dia {}'.format(nome))
