# Lista com import random

# import random
from random import choice as escolha
n1 = str(input("Nome: "))
n2 = str(input("Nome: "))
n3 = str(input("Nome: "))
n4 = str(input("Nome: "))
lista = [n1, n2, n3, n4]
pos = escolha(lista)
print("O nome sorteado foi {} !".format(pos))
