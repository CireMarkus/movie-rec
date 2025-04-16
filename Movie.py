class Movie:
    def __init__(self,title = None, director = None):
        self.title = title
        self.directors = []
        self.cast = []
        self.rtRating = None
        self.userRating = None
        self.genres = []
        if director:
            self.directors.append(director.split(',') if director.count(',') > 0 else director)
        
    def setTitle(self,title):
        self.title = title
        
    def getTitle(self):
        return self.title
        
    def addActor(self,actor):
        self.cast.extend([actors.strip() for actors in actor.split(',') if actors not in self.cast])
    
    def getActors(self):
        return self.cast
        
    def addDirector(self, director):
        if None not in self.directors:
            self.directors.extend([directors.strip() for directors in director.split(',') if directors not in self.directors])
        else:
            self.directors=[directors.strip() for directors in director.split(',') if directors not in self.directors]

    def getDirectors(self):
        return self.directors
        
    def setRTRating(self,rating):
        self.rtRating = rating
    
    def getRTRating(self):
        return self.rtRating
        
    def setUserRating(self,rating):
        self.userRating = rating 
    
    def getUserRating(self):
        return self.userRating
        
    def setGenre(self,genre):
        #TODO:add ability to differentiate between lists and strings.
        if isinstance(genre, list):
            # Check if genre is a list
            # If it's not already in the list, append it
            self.genres.extend(genre not in self.genres)
        elif genre not in self.genres:
            # Check if genre is a string
            # If it's not already in the list, append it
            self.genres.extend([genres.strip() for genres in genre.split(',') if genres not in self.genres])
        
    def getGenre(self):
        return self.genres

    def __lt__ (self,other):
        return self.title < other.getTitle()
    
    def __gt__ (self,other):
        return self.title > other.getTitle()
    def __eq__ (self,other):
        return self.title == other
    
    def to_dict(self):
        movie_dict = {}
        movie_dict['title'] = self.title
        movie_dict['director'] = self.directors
        movie_dict['actors'] = self.cast
        movie_dict['RTR'] = self.rtRating
        movie_dict['userRating'] = self.userRating
        movie_dict['genre'] = self.genres
        
        return movie_dict 