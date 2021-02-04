from ZODB import FileStorage, DB


class app_db(object):
    def __init__(self, path='/home/hme/data/Data.fs'):
        self.storage = FileStorage.FileStorage(path)
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.dbroot = self.connection.root()

    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()