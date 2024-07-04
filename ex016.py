# digitar um número 1,2354 imprimir 1
import math
num = float(input("Digite um número: "))
print("O número digita foi {}, sua parte inteira é: {:.0f}".format(num, math.floor(num)))
print("O número digita foi {}, sua parte inteira  truncada é: {}".format(num, math.trunc(num)))
