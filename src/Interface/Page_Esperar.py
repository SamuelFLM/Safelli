import PySimpleGUI as sg

def page_esperar():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("TIME: ",pad=(20,(20,20)),font="verdana 11 bold"),sg.Slider((0,20), orientation='h', s=(10,15),pad=(20,(0,15)),key="valorTime")],
        [sg.Image(filename="img/add_button.png",
                 size=(64, 64), pad=(120,(0,0)), enable_events=True, key='okClique',)]
    ]


    window = sg.Window('', layout, size=(300,150),finalize=True, font="verdana 11 bold", no_titlebar=True,grab_anywhere = True,icon="")
    return window