from Interface.home import * 
import PySimpleGUI as sg

window = home()
while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'play':
        print("play mermao")
    if event == 'new':
        print("new mermao")