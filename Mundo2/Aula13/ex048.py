# Exercício Python 48: 
# Faça um programa que calcule a soma entre todos os números 
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 #Acumulador
for c in range (1, 500):
   if c % 3 == 0:
        soma += c
print('A soma de todos os valores é {}'.format(soma))


