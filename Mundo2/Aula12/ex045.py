# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Sua Opções: 
      [ 0 ] - Pedra
      [ 1 ] - Papel
      [ 3 ] - Tesoura''')

jogador = int(input('Qual é seu palpite? '))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0: #jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Inválida')

if computador == 1: #jogou Papel
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada Inválida')

if computador == 2: #jogou Tesoura
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida')
