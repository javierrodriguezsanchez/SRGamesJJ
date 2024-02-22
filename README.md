# SRGamesJJ

### Authors:
- Javier Rodríguez Sánchez
- Jorge Alberto Aspiolea González

### IRS model definition:

This poject is a videogame recomendation system made in python, using the clasic vector space model for search and recomend the products listed, with a gui implemented with the PySimpleGUI python library.

### Considerations made in the implementation
- The interface will only return the top 10 best matches.
- The search and the recomendation are separated, the previus search  is not taken into account when making a query.
- The recomendations are only based on the categories and the titles of the games that the user download, not in the plot.
- The ranking of the game is taked in account in order to search and recomend. Those who has better ranking has more probability to apear.
- The user can filter the results based on the categories of the game wanted.

### How to  Run the Project:

### Our solution

- At first, there was a preprocessing of the original data:
    - Removing all the videogames with missing plots.
    - Solving the problem of the "See more details" at the end of some descriptions.
    - Removing duplicated elements.
    - Using nltk and gensim python librarys in order to get the vector representation of the data after being tokenized and removing noise and stopwords of the game plots. 
- Then, the query_processor was created
    - This class recieved a  query, and automatically turn it into a vector.
    - Then we calculate for each document the cosin similarity times the rating of the game.
    - Finally, we sort this list by values and return them.
- The recomendation process consist in:
    - The GUI allows the user to "download" games. This games are saved into a file as the preferences of the user
    - The recomendation is a search of the concatenation of the titles.
    - Also, the values of  the vectors are multiplied by a bonus given by the categories more liked by the users.

### Proposed improvements to the solution
- In the GUI
    - The interface only shows the top 10 results. One better improvement is the paginated of the results
    - The actual database does not include pictures of the videogame. Add images of them will improve the user experience
    - Give the user the option to erase his download historial in order to reset the recomendations
- In the search
    - One possible improvement is to use external fonts of information in order to relate words with the same meaning
    - The system have problems to detect spelling errors (e.g. search Barbi instead of Barbie). This problem could be manage with tries data structures and similarity algorithms (such as Levenstein distance algorithm).