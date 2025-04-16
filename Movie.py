class Movie:
    def __init__(self,title = None, director = None):
        self.title = title
        self.directors = []
        self.cast = []
        self.rtRating = None
        self.userRating = None
        self.genres = []
        self.directors.append(director.split(','))
        
    def setTitle(self,title):
        self.title = title
        
    def getTitle(self):
        return self.title
        
    def addActor(self,actor):
        self.cast.append(actor)
    
    def getActors(self):
        return self.cast
        
    def addDirector(self, director):
        if None not in self.directors:
            self.directors.append(director.split(','))
        else: 
            self.directors = director.split(',')
            
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
        if isinstance(genre, list):
            # Check if genre is a list
            # If it's not already in the list, append it
            for g in genre:
                if g not in self.genres:
                    self.genres.append(g)
        elif genre not in self.genres:
            # Check if genre is a string
            # If it's not already in the list, append it
            self.genres.append(genre)
        
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