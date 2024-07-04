soma = 0
for i in range(1,7):
    num = int(input('Digite o {} numero '.format(i)))
    result = (num % 2)
    if result == 0:
        soma = soma + num
print('O valor da soma dos números pares é {}'.format(soma))