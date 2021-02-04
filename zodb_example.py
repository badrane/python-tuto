from app_db import app_db


def print_album(album, details=True):
    print('Name: %s in %s ' % (album.name, album.year))
    if details:
        for track in album.tracks:
            print_track(track, details=False)
        print('')


def print_track(track, details=True):
    print('Title: %s by %s' % (track.title, track.artist))
    if details:
        for album in track.albums:
            print_album(album, details=False)
        print('')


db = app_db()
# iterate over albums and tracks
print('List of Albums')
for album in db.dbroot['Albums'].values():
    print_album(album)
print('List of Tracks')
for track in db.dbroot['Tracks'].values():
    print_track(track)
db.close()