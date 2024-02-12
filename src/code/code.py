import json
import os

def Recomendations(categories):
    Videogames =""
    my_path=os.path.abspath(__file__)
    path=my_path.replace('src/code/code.py','data/videogames_edited.json')
    with open(path,'r') as data:
        for letter in data:    
            Videogames+=letter
    Videogames=json.loads(Videogames)
    results=[game for game in Videogames if 
             all([cat in game['categories'] for cat in categories])]
    return sorted(results,key=lambda x:(Similarity(x),0 if x['rating'] == None else x['rating']),reverse=True)

def Similarity(game):
    return 0