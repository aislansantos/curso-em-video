# Curso Python #09 - Manipulando Texto

frase = 'Curso em Video Python'

####fatiamento de sting#####
print(('=' * 15) + 'Fatiamento de Strings' + ('=' * 15))
# pega somente a letra indicada
print(frase[9])


# pega do 9 ao 13 inclui o 9 e exclui o 13
print(frase[9:14])
print(frase[9:21])


# pega do no ao 21 pulando de 2 em 2 string
print(frase[9:21:2])


# quando eu não coloco onde vai começar que é o numero antes o : ele vai do zero até o indicado
print(frase[:5])


#dessa forma sem colocar aonde parar ele vai até o final da cadeia de string
print(frase[15:])


#começa no nove, como não tem o numero indicanto onde termina
#significa que vai começar no nove e vai até o final e pulando de 3 em 3
print(frase[9::3])


#analise de string
#é saber as informações das string
#por exemplo onde começa, quantos caracteres tem

#mostra o tamanho da string
print(len(frase))


#conta quantos o´s minusculo tem
print(frase.count('o'))


'''
dessa forma ele faz a contagem fazendo o fatiamento
nesse caso ele conta os o´s do zero a 13 excluindo a 13ª posição
o o de 'Video' é ma ultima letra ou seja 13º caractere ele volta uma
posição então só entra as letras ó até o Vid'E'o o e do video contando
uma letra do final de curso
'''
print(frase.count('o',0,13))


#mostra em que posição começa a sequencia "deo" de video
print(frase.find('deo'))


#se no find colocar uma string que não existe ele retorna o valor -1
print(frase.find('Android'))

#retona false ou true se existe a palavra ou sequencia, nesse caso não é uma funcionalidade e sim um operador
print('Curso' in frase)


#### transformação de sting #####
print(('=' * 15) + 'Transformação de Strings' + ('=' * 15))
#--> via de regra uma lista de string é imutavel, consegue- mudar ela atraves dos metodos mais não se conegue mexer direto nos elementos

'''
Replace = trocar / reposicionar:
no exemplo abaixo procuramos por "Python" e trocamos por "Android"
esse metodo não substitui direto na string, ele faz isso de forma secundaria

'''
print(frase.replace('Python', 'Android'))


# upper - coloca as letras em maiuscula todas as que estão em minuscula
print(frase.upper())

#lower - coloca as letras em minuscula todas que estão em maiuscula
print(frase.lower())

#capitalize - joga todos os caracteres pra minusculo só a primeira vai ficar maiuscula
print(frase.capitalize())

'''
title - faz uma analise um pouco mais profunda ele analisa quantas palvras tem essa string(pela posição dos espaços),
e vai colocar a primeira letra de cada palavra como maiuscula
'''
print(frase.title())

# string com algums espaços antes e depois das palavras que podem ser inuteis
frase_nova = "   Aprenda Python  "


#strip - remove espaços inuteis no inicio e no final da string
print(frase_nova.strip())

'''
rstrip - tem um R no inicio do comando strip, que pe de RIGHT, muitas funções tem a variação R no inicio das funções,
nesse caso remove os espaços da direita

'''
print(frase_nova.rstrip())


'''
lstrip - tem um R no inicio do comando strip, que pe de LEFT, muitas funções tem a variação L no inicio das funções,
nesse caso remove os espaços da esquerda
'''
print(frase_nova.lstrip())

#### Divisaão de strings #####
print(('=' * 20) + ' Divisão de Strings ' + ('=' * 20))

'''
split - separa e refaz o indices, ao inves de contar de 0 a 20 agora ele conta cada palavra como um item diferente,
aqui ele gera uma lista com todas as palavras que estão dentro da string cada palavra vira uma lista
'''
frase_split = frase.split()
print(frase_split)

#### Junção de strings #####
print(('=' * 20) + ' Junção de Strings ' + ('=' * 20))

'''
join - se eu tenho nomes separados em listas usando o join, juntamos todas as strings das listas
no exemplo abaixo estamos juntando a lista splitada anteriormente com "-" (hifem), mais podemos colocar
" " (espaço) dentro das aspas e voltar como era antes de DIVIDIR.
'''
print(frase_split)
print('-'.join(frase_split))
print(' ')
print(' ')


#### Texto grande #####
print(('=' * 20) + ' Printar Texto Grande ' + ('=' * 20))
print(' ')
# usando tres aspas duplas dentro do print podemos printar textos compridos conforme exemplo abaixo

print("""– Minha filha, o que você fará lá? Estarão
presentes todas as mais belas e ricas moças da corte.
Tire esta ideia insensata da cabeça; eu sei que você deve
estar sofrendo, mas não torne o sofrimento uma loucura.

E a filha respondeu:

Não, querida mãe, não estou sofrendo e muito menos
louca, eu sei que jamais poderei ser a escolhida,
mas é minha oportunidade de ficar pelo menos alguns
momentos perto do príncipe, isto já me torna feliz.""")