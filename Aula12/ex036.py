#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorImovel = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o valor do salário? '))
anos = int(input('Em quantos anos o financiamento do imóvel? '))

prestacao = casa / (anos * 12)
minimo = salario * 30/100

