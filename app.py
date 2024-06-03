import PySimpleGUI as sg

sg.theme('reddit')

#Criação da tela de login
tela_login = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*', key='senha')],
    [sg.Button('Enviar')],
    [sg.Output(size=(43,10))]
]

#Definição da janela de login
janela = sg.Window('Login', layout=tela_login)

#Validação de senha
while True:
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar':
        usuario_digitado = values['usuario']
        senha_digitada = values['senha']
