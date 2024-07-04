nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maículos é: {}'.format(nome.upper()))
print('Seu nome em minusculos é: {}'.format(nome.lower()))
print('Seu nome tem ao todo: {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem é: {} letras'.format(nome.find(' ')))

