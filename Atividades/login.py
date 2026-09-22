usuario = input('crie sua conta: ')
senha = input('crie sua senha: ')

while True:
    loginusuario = input('digite o nome da sua conta ')
    loginsenha = input('digite sua senha ')

    if loginusuario != usuario or loginsenha != senha:
        print('usuario ou senha invalido')
        continue
        
    if loginusuario == usuario and loginsenha == senha:
        print('login bem sussedido')
        break

