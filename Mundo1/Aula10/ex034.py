salario = float(input('Digite o valor do salário: '))
if (salario <= 1.250):
    novoSalario = (salario + (salario * 10 / 100))
else:
    novoSalario = (salario + (salario * 15 / 100))
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f} agora'.format(salario, novoSalario))