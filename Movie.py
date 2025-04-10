class Movie:
    def __init__(self,title = None, director = None):
        self.title = title
        self.directors = [director]
        self.cast = []
        self.rtRating = None
        self.userRating = None
        self.genres = []
        
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
            self.directors.append(director)
        else: 
            self.directors = [director]
            
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
        self.genres.append(genre)
        
    def getGenre(self):
        return self.genres

    def __lt__ (self,other):
        return self.title < other.getTitle()
    
    def __gt__ (self,other):
        return self.title > other.getTitle()
    def __eq__ (self,other):
        return self.title == other