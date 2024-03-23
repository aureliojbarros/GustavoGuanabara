# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos:

# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

#strip() - elimina os espaços antes de depois
#upper() - coloca os caracteres em maiúscula
#split() - divide a frase e cria uma lista []
#join() - une os items da lista

frase = str(input('Digite uma frase: ')).strip().upper() 
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase {}'.format(frase))
# inverso = ''
inverso = junto[::-1]
# for letra in range(len(junto)-1, -1, -1):
#     inverso += junto[letra]

if inverso == junto:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndrmo.')






