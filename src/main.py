from Interface.page.Home import * 
from Interface.page.Clicar import *
from Interface.page.Mouse import *
from Interface.page.Esperar import *
from Interface.page.Teclas import *
from Interface.page.Escrever import *
from Interface.page.Scroll import *
from Interface.page.NewProject import *
import PySimpleGUI as sg
import pyautogui as bot
algoritmo = []
lista_log = []
linhas = 0
# window = page_clicar()
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
        window.close()
        window = page_new_project()
        while True:
            event, values = window.read()    
            if event == "newproject" or event == "openproject":
                window.close()
                break
        window = home()
        
    # Janela Instrucoes
    if event == 'add':
        match(values["--OPCAO--"]):
            case "Mover Mouse":
                window.close()
                window = page_mouse()
                while True:
                    event, values = window.read()    
                    if event == "okClique":
                        valorX = values["valorX"]
                        valorY = values["valorY"] 
                        linhas += 1
                        algoritmo.append(f'{linhas} - Mover(X:{valorX} Y:{valorY})')
                        window.close()
                        break
                window = home()
                window['algoritmo'].update(algoritmo)
            case "Esperar":
                window.close()
                window = page_esperar()
                while True:
                    event, values = window.read()    
                    if event == "okClique":
                        valorTime = values["valorTime"]
                        linhas += 1
                        algoritmo.append(f'{linhas} - Esperar({valorTime})')
                        window.close()
                        break
                window = home()
                window['algoritmo'].update(algoritmo)
            case "Clicar":
                window.close()
                window = page_clicar()
                while True:
                    event, values = window.read()    
                    if event == "okClique":
                        valorBotao = values["valorBotao"]
                        qtd_cliques = values["qtd_cliques"]
                        linhas += 1
                        algoritmo.append(f'{linhas} - Clique: Botao({valorBotao}) Qtd({qtd_cliques})')
                        window.close()
                        break
                window = home()
                window['algoritmo'].update(algoritmo)
            case "Apertar Tecla(S)":
                window.close()
                window = page_tecla()
                while True:
                    event, values = window.read()    
                    if event == "okClique":
                        tecla1 = values["tecla1"]
                        tecla2 = values["tecla2"]
                        linhas += 1
                        algoritmo.append(f'{linhas} - Tecla(s)({tecla1} + {tecla2})')
                        window.close()
                        break
                window = home()
                window['algoritmo'].update(algoritmo)
            case "Escrever":
                window.close()
                window = page_escrever()
                while True:
                    event, values = window.read()
                    escreva = ""
                    if bool(values["checkLinha"]) == True:
                        window["checkVariasLinhas"].update(disabled=True)
                        window["linha1"].update(disabled=False)
                        escreva = values["linha1"]
                        
                    # if values["checkVariasLinhas"] == True:
                    #     window["checkLinha"].update(disabled=True)
                    #     window["multilinha"].update(disabled=False)
                    #     escreva = values["multilinha"]
                           
                    if event == "okClique":
                        linhas += 1
                        algoritmo.append(f'{linhas} - Escreva({escreva})')
                        window.close()
                        break
                window = home()
                window['algoritmo'].update(algoritmo)
            case "Scroll":
                window.close()
                window = page_scroll()
                while True:
                    event, values = window.read()
                    scroll = values["scroll"]
                    if event == "okClique":
                        linhas += 1
                        algoritmo.append(f'{linhas} - Scroll({scroll})')
                        window.close()
                        break
                window = home()
                window['algoritmo'].update(algoritmo)
            case default:
                bot.confirm(title="ALERT",text="SELECIONE UMA INSTRUCAO!", buttons=["OK"])
            
    if event == 'remove':
        algoritmo.pop()
        window['algoritmo'].update(algoritmo)
    if event == 'help':
        print("help mermao")
        
    # Janela Mouse position - OK
    if event == "add_position":
        if (values["--TIME--"] >= 0 and values["nome_position"] != ""):
            if values["minimizar"]:
                window.minimize()
            bot.sleep(values["--TIME--"])
            lista_log.append(f'{values["nome_position"]}:{bot.position()}')
            window['log'].update(lista_log)
        else:
            bot.confirm(title="alert", text="ERRO: TEMPO E NOME SEM PREENCHIMENTO.", buttons=["OK"])
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