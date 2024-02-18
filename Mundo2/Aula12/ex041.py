#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia 
#o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
nascimento = int(input('Data de nascimento do atleta: '))
idade = atual - nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Você tem {} anos e pertence a categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e pertence a categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e pertence a categoria JÚNIOR.'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e pertence a categoria SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos e pertence a categoria MASTER.'.format(idade))

