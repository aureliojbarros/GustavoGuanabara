#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))

media = (m1 + m2) / 2

if media < 5.0:
    print('Sua média foi {} e você foi reprovado.'.format(media))
elif media >= 5.0 and media <= 6.9:
    print("Sua média foi {} e você está em recuperação".format(media)) 
else:
    print('Sua média foi {} e você foi aprovado'.format(media))