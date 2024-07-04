import random
num = int(input('Em que número eu pensei ? '))
pcNum = random.randint(0, 5)
print('O número pensado foi: {}'.format(pcNum))
if num == pcNum:
    print('Parabéns ! Você acertou o número {}.'.format(num))
else:
    print('Infelizmente você errou ! O número pensado foi: {}.'.format(pcNum))

