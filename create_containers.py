from app_db import app_db
import transaction
from BTrees.OOBTree import OOBTree

db = app_db()
dbroot = db.dbroot
dbroot['Albums'] = OOBTree()
dbroot['Tracks'] = OOBTree()
transaction.commit()
db.close()
