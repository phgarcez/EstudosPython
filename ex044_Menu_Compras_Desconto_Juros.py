preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
      [ 1 ] A VISTA
      [ 2 ] 2X CARTÃO
      [ 3 ] 3X OU MAIS NO CARTÃO''')
opcao = float(input(' ESCOLHA A OPÇÃO: '))
if opcao == 1:
    print('O valor da sua compra com desconto a vista é {}'.format(preco*0.95))
elif opcao == 2:
    print('O valor da sua compra parcelada em 2x é {} cada parcela será de {}'.format(preco * 1.05,preco * 1.05/2))
elif opcao == 3:
    parcelas = int(input('Digite o valor de parcelas: '))
    print('O valor da sua compra parcelada em {}x é {:.2f} cada parcela será de {:.2f}'.format((parcelas), (preco * 1.10), (preco * 1.10 / parcelas)))
