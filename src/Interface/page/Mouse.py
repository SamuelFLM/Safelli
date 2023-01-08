import PySimpleGUI as sg

def page_mouse():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("X: ", pad=(20,(50,30))), sg.Input("",s=(10,10),pad=(20,(50,30)), key="valorX")],
        [sg.Text("Y: ",pad=(20,(0,0)),font="verdana 11 bold"),sg.Input("",s=(10,10),pad=(20,(0,15)),key="valorY")],
        [sg.Image(filename="src/Interface/page/img/buttons/add_button.png",
                 size=(64, 64), pad=(150,(30,0)), enable_events=True, key='okClique',)]
    ]


    window = sg.Window('', layout, size=(400,250),finalize=True, font="verdana 11 bold", no_titlebar=True,grab_anywhere = True,icon="")
    return window