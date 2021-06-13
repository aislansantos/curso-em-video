# Tabalhar empacotamento em lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somanso os valores {valores} temos {s}')


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

print()
print()

soma(5, 2)
soma(2, 9, 4)
