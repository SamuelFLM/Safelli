import PySimpleGUI as sg

def page_clicar():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Botao: ", pad=(20,(50,30))), sg.OptionMenu(["Esquerdo", "Direito"], key="valorBotao",pad=(20,(50,30)))],
        [sg.Text("Quantidade Cliques: ",pad=(20,(0,0)),font="verdana 11 bold"),sg.Slider((0,3), orientation='h', s=(10,15),pad=(20,(0,15)),key="qtd_cliques")],
        [sg.Image(filename="src/Interface/page/img/buttons/add_button.png",
                 size=(64, 64), pad=(150,(30,0)), enable_events=True, key='okClique',)]
    ]


    window = sg.Window('', layout, size=(400,250),finalize=True, font="verdana 11 bold",no_titlebar=True, grab_anywhere = True,icon="")
    return window