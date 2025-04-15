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
                genre_dict[datum] = set(data[datum])
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
            movie = Movie(datum['title'])
            
            if type(datum['director']) == str:
                movie.addDirector(datum['director'])
            else:
                for director in datum['director']:
                    movie.addDirector(director)

            for actor in datum['actors']:
                movie.addActor(actor)
                
            movie.setRTRating(datum['RTR'])
            
            try:
                movie.setUserRating(datum['userRating'])
            except KeyError:
                movie.setUserRating(None)

            for genre in datum['genre']:
                movie.setGenre(genre)
                
            node = Node(movie)
            movie_tree.add_node(node)

def save_genre_dict():
    '''
    Save the genre dictionary to a json file for later use. 
    Will also create a new file if it does not exist.
    '''  
    for i in genre_dict:
        #convert the set to a list
        genre_dict[i] = list(genre_dict[i])
    with open('Genre.json', 'w') as file:
        #create a list of dictionaries to save the genre dictionary
        #dump the data to the json file
        json.dump(genre_dict, file, indent=4)

def save_movies():
    '''
    save the movies to a json file for later use.
    Will also create a new file if it does not exist.
    '''
    with open('Movies.json', 'w') as file:
        #create a list of dictionaries to save the movies
        movie_list = Movies.inorder_trav(Movies.root)
        data = []
        for movie in movie_list:
            data.append(movie.to_dict())
        #dump the data to the json file
        json.dump(data, file, indent=4)
        #create a list of dictionaries to save the movies
    
    
def main():
    pass

if __name__ == "__main__":
    load_movies(Movies)
    
    movie_list = Movies.inorder_trav(Movies.root)
    for i in movie_list:
        print(i.getTitle(),i.getGenre())
        i.addDirector("Eric Washington")
    
    load_genres()
    print(genre_dict)

    save_genre_dict()
    save_movies()
    