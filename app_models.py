from persistent import Persistent


class Track(Persistent):
    def __init__(self, title, artist=None, albums=[]):
        self.title = title
        self.artist = artist
        self.albums = albums

    def add_album(self, album):
        self.albums.append(album)
        self._p_changed = 1


class Album(Persistent):
    def __init__(self, name, year=None):
        self.name = name
        self.year = year
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)
        self._p_changed = 1