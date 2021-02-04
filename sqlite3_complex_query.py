import sqlite3

db = sqlite3.connect(r'chinook.sqlite')


# -- row factory
db.row_factory = sqlite3.Row
cursor = db.cursor()

cursor.execute('''
        select title as album,
        group_concat(distinct genre.name) as genres
        from      track
             join genre using(genreid)
             join album using(albumid)
        group by title
        having count(distinct genre.name) > 1;
''')
for row in cursor:
    #
    print('{0} ==> {1}'.format(row['album'], row['genres']))

db.commit()
db.close()


