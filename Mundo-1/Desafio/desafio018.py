from math import radians, sin, cos, tan
angulo = int(input('Digite o angulo: '))


seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O angulo digitado foi: {}, o seno dele é {:.2f}, o consseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))