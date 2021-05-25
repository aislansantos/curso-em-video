# programa que faça a media de duas notas de um aluno

n1 = float(input('Digite 1ª nota: '))
n2 = float(input('Digite 2ª nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print('A media do aluno é: {} - Aprovado!'.format(media))
else:
    print('A media do aluno é: {} - Reprovado!'.format(media))