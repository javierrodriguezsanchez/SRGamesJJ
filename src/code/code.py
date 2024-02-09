import json
#code

def Recomendations(categories):
    Videogames =""
    with open('../../data/videogames_edited.json','r') as data:
        for letter in data:    
            Videogames+=letter
    Videogames=json.loads(Videogames)
    results=[game for game in Videogames if 
             all([cat in game['categories'] for cat in categories])]
    return sorted(results,key=lambda x:(Similarity(x),0 if x['rating'] == None else x['rating']),reverse=True)

def Similarity(game):
    return 0