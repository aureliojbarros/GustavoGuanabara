#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e 
#peça para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal.

num = (int(input('Digite um número: ')))
print('''Escolha uma das bases para conversão: 
      [1] - para Binário
      [2] - para Octal
      [3] - Hexadecimal''')

opcao = int(input('Digite a opção: '))
if opcao == 1:
    print('A conversão do número inteiro {} para binário é {}'.format(num, bin(num)[:2]))
elif opcao == 2:
      print('A conversão do número inteiro {} para octal é {}'.format(num, oct(num)[:2]))
elif opcao == 3:
     print('A conversão do número {} para hexadecimal é {}'.format(num, hex(num)[:2]))
else:
     print('Você escolheu uma opção inválida. Tente outra vez.')