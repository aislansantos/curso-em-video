#empacotamento de parametros
# no exemplo abaixo por padrão a sequencia é tranformada em tupla
def contador(*num):
    tam= len(num)
    print(f'Recebi os valor {num} e são ao todo {tam}')
    for valor in num:
        print(f'{valor}', end=' ')
    print()
    print()
    
    

contador(5,7,3,1,4)
contador(8,4,7)
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)