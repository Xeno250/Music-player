from album import Album
from song import Song

class MusicPlayer:
  def play(self, albums):
    for album in albums:
      for song in album.songs:
        print(f"Playing: {song.name}")
