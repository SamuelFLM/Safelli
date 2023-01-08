import PySimpleGUI as sg

def page_new_project():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("SELECIONE", pad=(130,(20,20)))],
        [sg.Button("NEW PROJECT",pad=(20,(50,30)), key="newproject"), sg.Button("OPEN PROJECT",pad=(20,(50,30)), key="openproject")],
    ]


    window = sg.Window('', layout, size=(400,250),finalize=True, font="verdana 11 bold", no_titlebar=True,grab_anywhere = True,icon="")
    return window