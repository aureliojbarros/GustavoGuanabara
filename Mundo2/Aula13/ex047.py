# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for numeros in range (0,51):
    if numeros % 2 == 0:
        print(numeros, end=' ')