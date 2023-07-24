import moeda


n = float(input('Digite um Preço: '))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O triplo de {n} é {moeda.triplo(n)}')
print(f'Aumentando 15%, temos {moeda.aumentar(n,15)}')
