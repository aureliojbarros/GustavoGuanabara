
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

maior = a
if (b > a and b > c):
    maior = b
if (c > a and c > b):
    maior = c
menor = a
if (b < a and b < c):
    menor = b
if (c < a and c < b):
    menor = c

print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))