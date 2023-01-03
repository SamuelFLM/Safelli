import PySimpleGUI as sg

def page_tecla():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Teclas: ",pad=(20,(50,30))),sg.OptionMenu(["Ctrl", "win", "alt", "Fn", "Shift", "Enter", "Tab", "Esc"], pad=(20,(50,30)),key="tecla1"),sg.Input("" , size=(10,10),pad=(0,(50,30)),key="tecla2")],
        [sg.Image(filename="img/add_button.png",
                 size=(64, 64), pad=(150,(30,0)), enable_events=True, key='okClique',)]
    ]


    window = sg.Window('', layout, size=(400,250),finalize=True, font="verdana 11 bold", no_titlebar=True,grab_anywhere = True,icon="")
    return window