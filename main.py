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
            data = json.load(file)
            #load the data into the genre dictionary
            for datum in data: 
                genre_dict[datum['genre']] = set(datum['movies'])
    except FileNotFoundError:
        movie_list = Movies.inorder_trav(Movies.root)
        #check to see if the movie tree is empty
        if not movie_list:
            print("The movie tree is empty.")
            return
        #traverse the movie tree and add the genres to the genre dictionary
        # add movie to each of the generes that it fits
        for movie in movie_list:
            for genre in movie.getGenre():
                if genre not in genre_dict:
                    genre_dict[genre] = set()
                genre_dict[genre].add(movie.getTitle())
    except Exception as e:
        #catch any other exceptions and print the error message
        print(f"unexpected error: {e}, type: {type(e)}")
        raise e
        

    
    

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
            
            for actor in datum['actors']:
                movie.addActor(actor)
                
            movie.setRTRating(datum['RTR'])
            
            for genre in datum['genre']:
                movie.setGenre(genre)
                
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
    
    load_genres()
    print(genre_dict)

    