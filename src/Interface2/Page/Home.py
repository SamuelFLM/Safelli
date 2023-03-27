import PySimpleGUI as sg

def page_inicial():
    backgroud = background_color="#0E0C23"
    layout_icon = [
        [sg.Image(filename="src/Interface2/Image/Icon/OFF/menu.png", background_color=backgroud, pad=(20,(20,20)), enable_events=True, key="menu")],
        [sg.Image(filename="src/Interface2/Image/Icon/OFF/home.png", background_color=backgroud, pad=(20,(20,20)), enable_events=True, key="home", visible=False)],
        [sg.Image(filename="src/Interface2/Image/Icon/OFF/terminal.png", background_color=backgroud, pad=(20,(20,20)), enable_events=True, key="terminal", visible=False)],
        [sg.Image(filename="src/Interface2/Image/Icon/OFF/log.png", background_color=backgroud, pad=(20,(20,20)), enable_events=True, key="log", visible=False)],
        [sg.Image(filename="src/Interface2/Image/Icon/OFF/config.png", background_color=backgroud, pad=(20,(20,20)), enable_events=True, key="config", visible=False)],
        [sg.Image(filename="src/Interface2/Image/Icon/OFF/sair.png", background_color=backgroud, pad=(20,(20,20)), enable_events=True, key="sair", visible=False)],
        
    ]

    layout = [
        [sg.Text("", pad=(160,(20,20)), background_color=backgroud),sg.Image(filename="src/Interface2/Image/Logo/mark-github-24.png",background_color=backgroud), sg.Image(filename="src/Interface2/Image/Logo/SAMUELFLM.png",background_color=backgroud)],
        [sg.Col(layout_icon, background_color=backgroud), sg.VSep()]
    ]
    window = sg.Window("a", layout=layout, finalize=True, grab_anywhere=True, size=(877,619), background_color=backgroud, font="verdana 11 bold")
    return window

window = page_inicial()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == "menu":
        window["menu"].update(filename="src/Interface2/Image/Icon/ON/menu.png")
        window["home"].update(visible=True)
        window["terminal"].update(visible=True)
        window["log"].update(visible=True)
        window["config"].update(visible=True)
        window["sair"].update(visible=True)