# 10.	Create a class that represents pieces of music. 
# Define a class constructor that allows you to set the initial values of the music piece (artist, track title, album, year) when the object is created. 
# Complete the class with the __str__ method returning the song data as a string, in the format as below (4 lines). 
# Then, create two objects that represent two different pieces of music. 
# Display these objects. 

class Song():
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    def __str__(self):
        return f"Performer: \t {self.artist}\nSong: \t\t {self.track_title}\nAlbum:\t\t {self.album}\nYear: \t\t {self.year}"

song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
song2 = Song("The Mamas & the Papas", "California Dreamin'", "California Dreamin'", "1965")
print(song1)
print()
print(song2)
