from Interface.home import * 
import PySimpleGUI as sg
import pyautogui as bot
lista_log = []
window = home()
while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    
    # Abaixo do log position
    if event == 'play':
        print("play mermao")
    if event == 'clear':
        print("clear mermao")
    if event == 'new':
        print("new mermao")
        
    # Janela Instrucoes
    if event == 'add':
        print("add mermao")
    if event == 'remove':
        print("remove mermao")
    if event == 'help':
        print("help mermao")
        
    # Janela Mouse position
    if event == "play_position":
        if values["minimizar"]:
            window.minimize()
        bot.sleep(values["--TIME--"])
        lista_log.append(f'{values["nome_position"]}:{bot.position()}')
        window['log'].update(lista_log)
    if event == "remove_position":
        try:
            lista_log.pop()
            window['log'].update(lista_log)
        except IndexError:
            pass
    if event == "help_position":
        bot.confirm(
            text="""
                EXPLICACAO SOBRE OS PARAMETROS
            
            TEMPO: CRONOMETRA O TEMPO PARA O USUARIO POSICIONAR O MOUSE NO LOCAL DESEJADO.\n
            NOME: O USUARIO PODE INDICAR UM NOME PARA AQUELA POSICAO.\n
            MINIMIZAR: MINIMIZA TELA NO MOMENTO DO PLAY.\n
            BOTAO PLAY: INICIA O CRONOMETRO PARA USUARIO POSICIONAR O MOUSE.\n
            BOTAO REMOVE: REMOVE DO LOG A ULTIMA POSICAO.\n
            """,
            title="POSICAO MOUSE",
            buttons=["OK"]
        )        