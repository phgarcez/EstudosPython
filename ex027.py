nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Seu primeiro nome é: {}.' .format(n[0]))
ultimo = len(n) - 1
# print(ultimo)
print('Seu último nome é {}.'.format(n[ultimo]))


