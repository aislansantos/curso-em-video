import os
os.system('cls' if os.name == 'nt' else 'clear')
# Parte prática
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 2 in num:
    num.remove(2)
else:
    print('Não achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')