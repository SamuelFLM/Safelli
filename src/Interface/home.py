import PySimpleGUI as sg
def home():
    sg.theme("Reddit")  # please make your windows colorful
    layout_esquerda = [
        [sg.OptionMenu(
            ["Mover Mouse","Esperar","Clicar","Apertar Tecla(S)", "Escrever","Scroll"],key="--OPCAO--")
        ],
    ]
    layout_direita = [
        [sg.Multiline(s=(25,20), pad=(0,(20,0)))],
        [sg.Image(filename="img/play.png",
                 size=(64, 64), pad=(10,(0,0)), enable_events=True, key='play',),
         sg.Image(filename="img/clear.png",
                 size=(64, 64), pad=(5,(0,00)), enable_events=True, key='clear',),
         sg.Image(filename="img/newfile_button.png",
                 size=(64, 64), pad=(5,(0,00)), enable_events=True, key='new',)]
    ]
    layout = [
        [sg.Image("img/Screenshot_1.png",size=(80,80),pad=(350,(0,0))),sg.Text("")],
        [sg.Text("SAFELLI",font="verdana 13 bold",pad=(350,(0,10)), text_color="#000080")],
        [sg.HSep(color="#000080")],
        [
            sg.Col(layout_esquerda,element_justification='left', justification='left',pad=(100,(0,0))),
            sg.VSep(color="#000080",pad=(0,(0,0))),
            sg.Col(layout_direita,pad=(20,(0,0)))
        ],
    ]
    window = sg.Window('Window Title', layout, size=(800,600),finalize=True, font="verdana 11 bold", grab_anywhere = True,icon="")
    return window