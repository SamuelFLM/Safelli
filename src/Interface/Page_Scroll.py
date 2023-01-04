import PySimpleGUI as sg

def page_scroll():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Valor Pixel: ", pad=(20,(50,30))), sg.Input("",s=(10,10),pad=(20,(50,30)), key="scroll")],
        [sg.Image(filename="img/add_button.png",
                 size=(64, 64), pad=(150,(30,0)), enable_events=True, key='okClique',)]
    ]


    window = sg.Window('', layout, size=(400,250),finalize=True, font="verdana 11 bold", no_titlebar=True,grab_anywhere = True,icon="")
    return window