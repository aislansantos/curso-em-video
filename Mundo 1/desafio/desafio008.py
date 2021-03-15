# Programa que converte metros em centrimetos e milimetros
medida = float(input('Digite um numero em metros: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {} metros, convertida é de {} km, {} hm, {} dam, {} dm,  {} centimetros e {} milimetros'.format(medida,km,hm, dam,dm, cm, mm))