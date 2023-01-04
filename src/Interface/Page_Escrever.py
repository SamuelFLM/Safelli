import PySimpleGUI as sg

def page_escrever():
    sg.theme("DarkBlue")
    layout = [
        [sg.Checkbox("Uma Linha: ", pad=(20,(50,30)), key="checkLinha"), sg.Checkbox("Varias Linha: ", pad=(20,(50,30)), key="checkVariasLinhas")],
        [sg.Input("",pad=(20,(0,0)),s=(20,20),font="verdana 11 bold", disabled=True,key="linha1")],
        [sg.Multiline("",pad=(20,(0,0)),s=(10,10),font="verdana 11 bold", disabled=True, key="multilinha")],
        [sg.Image(filename="img/add_button.png",
                 size=(64, 64), pad=(150,(30,0)), enable_events=True, key='okClique',)]
    ]


    window = sg.Window('', layout, size=(800,800),finalize=True, font="verdana 11 bold", no_titlebar=True,grab_anywhere = True,icon="")
    return window