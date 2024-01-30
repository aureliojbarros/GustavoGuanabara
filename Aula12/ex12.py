nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é normal.')
print('Tenha um bom dia, {}'.format(nome))

