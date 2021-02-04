from app_db import app_db
from app_models import Album, Track
import transaction
db = app_db()
albums = db.dbroot['Albums']
tracks = db.dbroot['Tracks']
tracks['Blowing in the Wind'] = Track('Blowing in the Wind', artist='Bob Dylan')
tracks['Like a Rolling Stone'] = Track('Like a Rolling Stone', artist='Bob Dylan')
# the key can be any unique id
albums['U1'] = Album('Ultimate Collection')
# add relationships
album = albums['U1']
track = tracks['Blowing in the Wind']
track.add_album(album)
album.add_track(track)
track = tracks['Like a Rolling Stone']
track.add_album(album)
album.add_track(track)
transaction.commit()
db.close()