import json
from Movie import Movie
from Node import Node
from Tree import Tree


genre_dict = {}
Movies = Tree()

def menu():
    '''
    Function to display the menu to the user.
    '''
    pass

def load_genres():
    '''
    Function to populate the genre dictionary with the genres of the movies.
    '''
    #check to see if there is a genre .json file 
    try:
        #if there is a file load the genre dictionary from the file
        with (open('Genre.json', 'r')) as file:
            pass
    except FileNotFoundError:
    #if there is not a file traverse the movie tree 
        #  to populate the genre dictionary with genres and movies that fit said genre
        # add the genres to the genere dictionary as a set
        pass
        

    
    

def load_movies(movie_tree):
    '''
    Load the movies from the json file into the movies tree
    '''
    #Pull the data from the json file
    with open('Movies.json', 'r') as file:
        data = json.load(file)
        
    
        #load the data into the movies tree
        for datum in data:
            movie = Movie(datum['title'], datum['director'])
            
            for i in datum['actors']:
                movie.addActor(i)
                
            movie.setRTRating(datum['RTR'])
            
            for i in datum['genre']:
                movie.setGenre(i)
                
            node = Node(movie)
            movie_tree.add_node(node)

def save_genre_dict():
    '''
    Save the genre dictionary to a json file for later use. 
    Will also create a new file if it does not exist.
    '''  
    #try dumping the genre dictionary to a json file? 

def save_movies():
    '''
    save the movies to a json file for later use.
    Will also create a new file if it does not exist.
    '''
    #try dumping the movie tree to a json file?
    
    
def main():
    pass

if __name__ == "__main__":
    load_movies(Movies)
    
    movie_list = Movies.inorder_trav(Movies.root)
    for i in movie_list:
        print(i.getTitle(),i.getGenre())

    