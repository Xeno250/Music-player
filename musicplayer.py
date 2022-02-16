from album import Album

class MusicPlayer:
  def __init__(self):
    self.albums = [
      Album()
    ]

  def play(self):
    for album in self.albums:
      for song in album.songs:
        print(f"Playing: {song.name}")
