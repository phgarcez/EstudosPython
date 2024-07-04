num1 = (input('Digite valor 1: '))
num2 = (input('Digite valor 2: '))
num3 = (input('Digite valor 3: '))
if num1 > num2 and num1 > num3:
    print('O numéro {} é o maior'.format(num1))
elif num2 > num3:
    print('O numéro {} é o maior'.format(num2))
else:
    print('O numéro {} é o maior'.format(num3))
