import json
from Movie import Movie
from Tree import Tree


genre_dict = {}
Movies = Tree()

def menu():
    '''
    Function to display the menu to the user.
    '''
    pass

def populate_genre_dict():
    '''
    Function to populate the genre dictionary with the genres of the movies.
    '''
    pass

def load_movies():
    '''
    Load the movies from the json file into the movies tree
    '''
    with open('movies.json', 'r') as file:
        data = json.load(file)
    #Pull the data from the json file
    #load the data into the movies tree
    pass

def save_genre_dict():
    '''
    Save the genre dictionary to a json file for later use. Will also create a new file if it does not exist.
    '''
    pass

def load_genre_dict():
    #load the genre dictionary from a json file
    pass


def main():
    pass

if __name__ == "__main__":
    pass