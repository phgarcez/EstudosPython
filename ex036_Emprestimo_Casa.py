casa = float(input('Qual valor da casa ? '))
salario = float(input('Qual seu salário ? '))
ano = float(input('Quantos anos para pagamento ? '))
meses = ano * 12
prestacao = casa / meses
porcentagem = salario * 0.3
if prestacao > porcentagem:
    print('Empréstimo negado, o valor da prestação {:.2f} é maior que 30% ({}) do salário'.format(prestacao, porcentagem))
else:
    print('Empréstimo liberado !')
    print('Valor da prestação: {:.2f} a ser em pago em {} meses'.format(prestacao, meses))
