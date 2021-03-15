import math
cateto_oposto = float(input('Digite o valor do cateto oposto '))
cateto_adjacente = float(input('Digite o numero do cateto adjacente '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('A hipotensa de triangulo retando com cateto oposto de {} e cateto adjacente de {} é de {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))