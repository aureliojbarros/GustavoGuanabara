#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year #Qual o ano atual?
idade = int(input('Digite sua idade: '))
nascimento = int(input('Digite a data de seu nascimento: '))
idade = atual - nascimento
print('Hoje você tem {} anos'.format(idade))
if idade == 18:
    print('Você está apto para o Serviço Militar.')
elif idade > 18:
    print('Você já passou no período do alistamento militar!')


