from artist import Artist
from song import Song

class Album:
  def __init__(self, artist, songs, name, year):
    self.artist = artist
    self.songs = songs
    self.name = name
    self.year = year