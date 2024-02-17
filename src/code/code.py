import json
import os
import ast
from code.query_processor import query_processor

def init_DG():
    Videogames = ""
    my_path=os.path.abspath(__file__)
    
    # path=my_path.replace('/src/code/code.py','data/Recomendations.json')

    path=my_path.replace('src\code\code.py','data\Recomendations.json')
    
    with open(path,'r') as data:       
        for letter in data:   
            Videogames+=letter
    Videogames=json.loads(Videogames)
    categories={'fantasy':0,'adventure':0,'comedy':0,'mystery':0,'family':0,
                'action':0,'crime':0,'sci-fi':0,'thriller':0}
    for x in Videogames:
        for cat in x['categories']:
            categories[cat]+=1
    return set(map(lambda x:x['name'],Videogames)),categories


def Recomendations(categories):
    DG,M=init_DG()
    Videogames =""
    my_path=os.path.abspath(__file__)
        
    # path=my_path.replace('src/code/code.py','data/videogames_edited.json')

    path=my_path.replace('src\code\code.py','data\\videogames_edited.json')
    
    with open(path,'r') as data:
        for letter in data:    
            Videogames+=letter
    Videogames=json.loads(Videogames)
    results=[game for game in Videogames if all([cat in game['categories']
        for cat in categories]) and game['name'] not in DG]
    return sorted(results,key=lambda x:Similarity(x,M),reverse=True)

def Similarity(game,M):
    a=0
    for cat in game['categories']:
        a+=M[cat]
    return (a,0 if game['rating'] == None else game['rating'])

def Download(game):
    Videogames = ""
    my_path=os.path.abspath(__file__)
    
    # path=my_path.replace('code.py','Recomendations.json')

    path=my_path.replace('src\code\code.py','data\Recomendations.json')
    
    with open(path,'r') as data:       
        for letter in data:   
            Videogames+=letter
    Videogames=json.loads(Videogames)
    Videogames.append(ast.literal_eval(game))
    with open(path,'w') as data:
        json.dump(Videogames,data)

def Search(query,categories):
    Videogames = ""
    my_path=os.path.abspath(__file__)

    # path=my_path.replace('code.py','videogames_edited.json')

    path=my_path.replace('src\code\code.py','data\\videogames_edited.json')

    with open(path,'r') as data:       
        for letter in data:   
            Videogames+=letter
    Videogames=json.loads(Videogames)
    results=query_processor(query=query).matched_docs()
    for result in results:
        game=Videogames[result]
        if all([cat in game['categories'] for cat in categories]):
            yield game