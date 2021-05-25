diaria = int(input('Dias do carro alugado: '))
rodagem = float(input('Km rodados: '))

total_diaria = diaria * 60
total_rodagem = rodagem * 0.15


aluguel_total = total_diaria + total_rodagem

print('o valor total da locação do Veiculo é de R$ {:.2f}'.format(aluguel_total))