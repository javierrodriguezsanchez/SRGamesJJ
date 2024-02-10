import PySimpleGUI as sg
from itertools import islice
from code import Recomendations

#Current categories in database. If the categories changes, you must edit this list
#----------------------------------------------------------------------------------
categories=['fantasy','adventure','comedy','mystery','family',
                'action','crime','sci-fi','triller']


#--------------------------------------
#Functions that need to call the engine
#--------------------------------------

def RecomendationsGUI(categories_selected):
    for i in Recomendations(categories_selected):
        yield Show(i)

def Search(query,selected_categories):
#this function manage the query made by the user
    #Call the corresponding query function
    return []

def Show(game):
    layout=[
        [
            sg.Text('year: '),sg.Text(game['year']),
            sg.Text('rating: '),sg.Text(game['rating']),
        ] + [sg.Button(cat) for cat in game['categories']]
    ]
    
    if game['plot']!='':
        layout+=[[sg.Column([[
            sg.Multiline(game['plot'],expand_x=True,size=(75,2),no_scrollbar=False),
            sg.Button('Download',button_color='Green',key='Download'+game['name'])
        ]],justification='r',expand_x=True)]]
    
    else:
        layout+=[[sg.Button('Download',button_color='Green',key='Download'+game['name'])]]
    
    return [sg.Frame(game['name'],layout=layout,element_justification='c',expand_x=True)]

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
    sg.Button('Search',font=('Arial',14))],
    [sg.Text('Recomended for You', font=('Helvetica',30),pad=3)],
    [sg.Column(list(islice(RecomendationsGUI([]),10)), scrollable=True, 
               vertical_scroll_only=True, key='scrollable_area',expand_x=True)]]

screen_width, screen_height = sg.Window.get_screen_size()
window2 = sg.Window('VPN', layout, element_justification='c',size=(screen_width*98//100, screen_height*9//10), grab_anywhere=True)

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
        layout=layout+[[sg.Column(list(islice(RecomendationsGUI([]),10)),
                   scrollable=True, vertical_scroll_only=True,
                   key='scrollable_area',expand_x=True)]]
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
        layout=layout+[[sg.Column(list(islice(Search(values['query'],selected_categories),10)),
                   scrollable=True, vertical_scroll_only=True,
                   key='scrollable_area',expand_x=True)]]
        window2.close()
        window2=sg.Window('VPN', layout, element_justification='c')
        window2.Resizable = True
        