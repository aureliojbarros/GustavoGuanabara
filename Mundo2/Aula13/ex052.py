# Exercício Python 52: 
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 

tot = 0
num = int(input('Digite um número: '))
for c in range (1, num + 1):
    if num % c == 0:
        print('O número {} / {} é primo '.format(num, c))
        tot += 1
    else:
        print('O número {} / {} não é primo '.format(num, c))
    # print('{} '.format(c), end='')