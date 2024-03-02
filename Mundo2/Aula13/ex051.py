# Exercício Python 51: 
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
# an = a1 + (n-1) * r

p1 = int(input('Digite o primeiro termo: '))
n = int(input('Digite a posição do termo a ser descoberto: '))
r = int(input('Digite a razão: '))
pa = p1 + (n - 1) * r # Fórmula da P.A.
for c in range (p1, n, r):
    print('{} '.format(c), end=' ->')
print('Fim')


