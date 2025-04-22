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
    print("Welcome to the Movie Recommendation System!")
    while True:
        print("Please select an option:")
        print("1. Add a movie")
        print("2. Find a movie by title")
        print("3. Recommend a movie by genre")
        print("4. Rate a movie")
        print("5. Print all movies")
        print("6. Exit")
        print("--------------------------------------------------")
        
        user_input = input("Enter your choice: ")
        
        if user_input == '1':
            add_movie(Movies)
        elif user_input == '2':
            title = input("Enter the title of the movie: ")
            find_movie_by_title(Movies, title)
        elif user_input == '3':
            recommend_movie_genre()
        elif user_input == '4':
            rate_movie()
        elif user_input == '5':
            movie_list = Movies.inorder_trav(Movies.root)
            print("Movies in the system:")
            print("--------------------------------------------------")
            for movie in movie_list:
                print(f"Title: {movie.getTitle()}")
                print("--------------------------------------------------")
        elif user_input == '6':
            print("Thank you for using the Movie Recommendation System!")
            save_movies()
            save_genre_dict()
            exit()
        else:
            print("Invalid choice. Please try again.")

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
    
#TODO: review and rewrite the load_movies function
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

def add_genre(movie):
    '''
    Function to add a genre to the genre dictionary.
    '''
    genres = movie.getGenre()

    #check to see if the genre is a list or a string
    if (isinstance(genres, list)):
        #if it is a list then add each genre to the genre dictionary
        for genre in genres:
            if genre not in genre_dict:
                genre_dict[genre] = set()
            genre_dict[genre].add(movie.getTitle())
    else:  
        #if it is a string then add the genre to the genre dictionary
        if genres not in genre_dict:
            genre_dict[genres] = set()
        genre_dict[genres].add(movie.getTitle())

#TODO:refactor to pass null values if the user skips inputting data. 
def add_movie(movie_tree):
    '''
    Function to add a movie to the tree.
    '''
    new_movie = Movie()
    title = input("Enter the title of the movie: ")
    new_movie.setTitle(title)
    director = input("Enter the director(s) of the movie as a comma seperated list: ")
    new_movie.addDirector(director)
    genres = input("Enter the genre(s) of the movie as a comma seperated list: ")
    new_movie.setGenre(genres)
    actors = input("Enter the actor(s) of the movie as a comma seperated list: ")
    new_movie.addActor(actors)
    rt_rating = input("Enter the Rotten Tomatoes rating of the movie: ")
    new_movie.setRTRating(rt_rating)
    user_rating = input("Enter the user rating of the movie: ")
    new_movie.setUserRating(user_rating)
    add_genre(new_movie)
    #TODO:check to see if the movie is alread in the tree. 

    node = Node(new_movie)
    movie_tree.add_node(node)
        
#TODO: Work on setting up the recommendation system 
def recommend_movie_genre():
    '''
    Function to recommend a movie to the user based on entered genres.
    '''
    print("Enter the genre(s) of the movie as a comma seperated list: ")
    genres = input()
    genres = genres.split(",")
    movie_recs = set()
    #check to see if the genre is in the genre dictionary
    for genre in genres:
        if genre not in genre_dict:
            print(f"{genre} is not a valid genre.")
            continue
        if len(movie_recs) == 0:
            movie_recs = genre_dict[genre]
        else:
            movie_recs = movie_recs.intersection(genre_dict[genre])
    
    print("The following movies are recommended for you: ")
    print("--------------------------------------------------")
    #loop through the movie recommendations and print the movie title, director, actors, and ratings
    for movie in movie_recs:
        find_movie_by_title(Movies, movie)
        print("--------------------------------------------------")

def find_movie_by_title(movie_tree, title):
    '''
    Function to find a movie by title.
    '''
    node = movie_tree.search(title)
    #if the movie is found then return the movie
    if node:
        print(f"Movie found: {node.getData().getTitle()}")
        print(f"Director(s): {node.getData().getDirectors()}")
        print(f"Actor(s): {node.getData().getActors()}")
        print(f"Rotten Tomatoes rating: {node.getData().getRTRating()}")
        print(f"User rating: {node.getData().getUserRating()}")
        print(f"Genre(s): {node.getData().getGenre()}")
    #if the movie is not found then return None
    else:
        print(f"{title} not found in the movie tree.")

def rate_movie():
    '''
    Function to rate a movie.
    '''
    title = input("Enter the title of the movie: ")
    node = Movies.search(title)
    #if the movie is found then return the movie
    if node:
        rating = input("Enter the rating of the movie: ")
        node.getData().setUserRating(rating)
        print(f"{title} has been rated {rating}.")
    #if the movie is not found then return None
    else:
        print(f"{title} not found in the movie tree.")

#TODO: Work on setting up the recommendation system based on the directors. 
# def recommend_movie_director():
#     '''
#     Function to recommend a movie to the user based on entered directors.
#     '''

#     pass

#TODO: Work on setting up the recommendation system based on the actors.
# def recommend_movie_actor():
#     '''
#     Function to recommend a movie to the user based on entered actors.
#     '''
#     pass






if __name__ == "__main__":
    load_movies(Movies)
    
    movie_list = Movies.inorder_trav(Movies.root)
    for i in movie_list:
        print(i.getTitle(),i.getGenre())
        i.addDirector("Eric Washington")
        i.addDirector("Yasmin Parker")
    print("\n\n\n")
    load_genres()

    for i in genre_dict:
        print(i, genre_dict[i])
    print("\n\n\n")
    
    
    find_movie_by_title(Movies, "The Matrix")
    print("\n\n")
    find_movie_by_title(Movies, "Mute")
    print("\n\n")
    recommend_movie_genre()
    print("\n\n")

    save_genre_dict()
    save_movies()
    