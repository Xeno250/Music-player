from musicplayer import MusicPlayer
from album import Album
from song import Song
from artist import Artist

def main():
  player = MusicPlayer()

  albums = []

  num_albums = int(input("How many albums? "))
  for i in range(num_albums):
    name = input("Album name: ")
    year = input("Year: ")

    artist = CreateArtist()
    songs = CreateSongs()
    album = Album(artist, songs, name, year)
    albums.append(album)

  player.play(albums)

def CreateArtist():
    name = input("Artists name: ")
    age = input("Artists age: ")
    artist = Artist(name, age)
    return artist

def CreateSongs():
  songs = []
  num_songs = int(input("How many songs? "))
  for i in range(num_songs):
    name = input("Song name: ")
    duration = input("Song duration: ")
    song = Song(name, duration)
    songs.append(song)

  return songs

main()