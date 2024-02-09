import PySimpleGUI as sg
#from code import Recomendations
from itertools import islice

#Current categories in database. If the categories changes, you must edit this list
#----------------------------------------------------------------------------------
categories=['fantasy','adventure','comedy','mystery','family',
                'action','crime','sci-fi','triller']


#--------------------------------------
#Functions that need to call the engine
#--------------------------------------

def RecomendationsGUI(categories_selected):
    global categories
    cat = categories if categories_selected==[] else categories_selected
    #for i in Recomendations(cat):
    for i in range(1,00):
        yield Show(i)

def Search(query,selected_categories):
#this function manage the query made by the user
    #Call the corresponding query function
    return []

def Show(game):
    return []

#------------------------------------------


#-------------------------------------------
#Auxiliar GUI Function for select categories
#-------------------------------------------

def SelectCategories():
#allows to chose the categories
    global categories
    layout=[[sg.Text("Caterories",font=('Helvetica',30))]]+[
           [sg.Checkbox(category, key=category) for category in categories[0:4]]
        ] + [[sg.Checkbox(category, key=category) for category in categories[4:]]
        ] + [[sg.Button('Select'),sg.Button('Cancel')]]
    window2=sg.Window('Select Categories',layout=layout,element_justification='c')

    accepted=[]
    while True:
        event, values = window2.read()
        
        if event=='Select':
            accepted= [category for category in categories if values[category]]
            window2.close()
            if accepted == [] or len(accepted)==len(categories):
                return []
            return accepted
        
        if event == sg.WIN_CLOSED or event=='Cancel' :
            window2.close()
            return None

selected_categories=[]
sg.theme('DarkAmber')
sg.set_options(font=('Arial Bold',18))

#------------------------------------------

#-----------------------------------------------------------------------
# ^   ^    ^    ===  ^   ¡     ===== .   . ^   ¡ ===== ===  /===\  ^   ¡
# |\ /|   / \    |   | \ |     |     |   | | \ |   |    |   |   |  | \ |
# | V |  /---\   |   |  \|     |==   |   | |  \|   |    |   |   |  |  \|
# !   ! /     \ ===  !   v     |      ===  !   v   !   ===  \===/  !   v
#-----------------------------------------------------------------------

layout = [
    [sg.Text('SR-GamesJJ', font=('Helvetica',50))],
    [sg.Text("Your best videogames collection",font=('Arial',18))],
    [sg.Button('Filter',font=('Arial',14)),sg.Input(key='query',size=(35,2)),
    sg.Button('Search',font=('Arial',14))],#[sg.Text('',key='categories',visible=False)]
] + list(islice(RecomendationsGUI([]),10))

window2 = sg.Window('VPN', layout, element_justification='c')

window2.Resizable = True
while True:
    event, values = window2.read()
    if event == sg.WIN_CLOSED:
        window2.close()
        break
    
    if event == 'Filter' :
        aux=SelectCategories()
        if aux==None:
            continue
        selected_categories=aux
        layout = [
            [sg.Text('SR-GamesJJ', font=('Helvetica',50))],
            [sg.Text("Your best videogames collection",font=('Arial',18))],
            [sg.Button('Filter',font=('Arial',14)),sg.Input(key='query',size=(35,2)),
            sg.Button('Search',font=('Arial',14))]]
        if selected_categories != []:
            layout=layout+[
            [[sg.Text('Categories:',font=('Arial',12),key='Categories:')]+
                [sg.Button(category,font=('Arial',10),key=category)
                for category in selected_categories]]
        ]
        layout=layout+list(islice(RecomendationsGUI(selected_categories),10))
        window2.close()
        window2=sg.Window('VPN', layout, element_justification='c')
        window2.Resizable = True

    if event == 'Search':
        if values['query'] == '':
            continue
        layout = [
            [sg.Text('SR-GamesJJ', font=('Helvetica',50))],
            [sg.Text("Your best videogames collection",font=('Arial',18))],
            [sg.Button('Filter',font=('Arial',14)),sg.Input(key='query',size=(35,2)),
            sg.Button('Search',font=('Arial',14))]]
        if selected_categories != []:
            layout=layout+[
            [[sg.Text('Categories:',font=('Arial',12),key='Categories:')]+
                [sg.Button(category,font=('Arial',10),key=category)
                for category in selected_categories]]
        ]
        layout=layout+Search(values['query'],selected_categories)
        window2.close()
        window2=sg.Window('VPN', layout, element_justification='c')
        window2.Resizable = True
        