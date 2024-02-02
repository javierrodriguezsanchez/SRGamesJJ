import PySimpleGUI as sg

sg.theme('DarkAmber')
sg.set_options(font=('Arial Bold',18))

categories=['RPG','Aventura','Shutter','Plataforma','Deportes']

layout = [
    [sg.Text('SR-GamesJJ', font=('Helvetica',50))],
    [sg.Text("Your best videogames collection",font=('Arial',18))],
    [sg.Button('Filter',font=('Arial',14)),sg.Input(key='ips',size=(35,2)),
    sg.Button('Search',font=('Arial',14))],
    [sg.Text("",key="Categories")]
]

window2 = sg.Window('VPN', layout, element_justification='c')

window2.Resizable = True
while True:
    event, values = window2.read()
    if event == sg.WIN_CLOSED or event=='Exit' :
        window2.close()
        break
    
    if event == 'Filter' :
        window2['Categories'].update(visible=True)

