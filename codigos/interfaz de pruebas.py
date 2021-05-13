

import PySimpleGUI as sg
sg.theme('Topanga')
layout = [
            [sg.Text('hola soy un texto'),sg.Image(r'1.png')],
            [sg.Input("texto default",do_not_clear=True, enable_events=True, key='hola_pepe'),sg.Input("hola",key='me_cago_en_las_moscas',enable_events=True,do_not_clear=True)],
            [sg.Multiline('This is what a Multi-line Text Element looks like', size=(45,5))],
            [sg.Button('Exit')]
         ]

window = sg.Window('chechu nominas').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if len(values['hola_pepe']) > 5:
        window.Element('hola_pepe').Update(values['hola_pepe'][:-1])
    if len(values['me_cago_en_las_moscas'])>7:
        window.Element('me_cago_en_las_moscas').Update(values['me_cago_en_las_moscas'][:-1])
window.Close()