#These file manage the logic and the access to data of the aplication.
#Interacts with GUI.py and uses the class query_processor to search and recomend.

import json
import os
import ast
from code.query_processor import query_processor

#-----------------------------------------------------------------------------

def init_DG():
# This function gets the names of the games downloaded by the user and
# certain magnitude of the categories most liked by the users
    Videogames = ""
    my_path=os.path.abspath(__file__)
    path=my_path.replace('src\code\code.py','data\Recomendations.json')
    
    with open(path,'r') as data:       
        for letter in data:   
            Videogames+=letter
    Videogames=json.loads(Videogames)
    categories={'fantasy':1,'adventure':1,'comedy':1,'mystery':1,'family':1,
                'action':1,'crime':1,'sci-fi':1,'thriller':1}

    # Counting the frequency of each category in the Videogames data
    for x in Videogames:
        for cat in x['categories']:
            categories[cat]+=1
    return set(map(lambda x:x['name'],Videogames)),categories

#-----------------------------------------------------------------------------

def Recomendations(categories):
    # This function returns recommended games based on the given categories
    DG,M=init_DG()
    query=' '.join(DG)#creating a query with all the names of the games
    return Search(query,categories,M)

#-----------------------------------------------------------------------------

def Download(game):
# This function save a given game to the Recommendations.json file
    Videogames = ""
    my_path=os.path.abspath(__file__)
    path=my_path.replace('src\code\code.py','data\Recomendations.json')
    with open(path,'r') as data:       
        for letter in data:   
            Videogames+=letter
    Videogames=json.loads(Videogames)
    Videogames.append(ast.literal_eval(game))
    with open(path,'w') as data:
        json.dump(Videogames,data)

#-----------------------------------------------------------------------------

def Search(query,categories, sugestions=None):
    # This function searches for games based on a given query and categories
    Videogames = ""
    my_path=os.path.abspath(__file__)
    path=my_path.replace('src\code\code.py','data\\videogames_edited.json')
    with open(path,'r') as data:       
        for letter in data:   
            Videogames+=letter
    Videogames=json.loads(Videogames)
    
    # Using the query\_processor module to process the query and find matching documents
    results=query_processor(query=query,sugestions=sugestions).matched_docs()
    
    for result in results:
        game=Videogames[result]
        # Filtering the results based on the given categories
        if all([cat in game['categories'] for cat in categories]):
            yield game