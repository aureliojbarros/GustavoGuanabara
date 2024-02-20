""" Exercício Python 44: 
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros """

print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
      [ 1 ] - à vista dinheiro/cheque
      [ 2 ] - à vista no cartão
      [ 3 ] - 2x no cartão
      [ 4 ] - 3x ou mais no cartão''')
opcao = int(input('Qual a opção de pagamento? '))

if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f}.'.format(preco, total))