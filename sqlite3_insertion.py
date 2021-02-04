import sqlite3

db = sqlite3.connect(r'chinook.sqlite')
#print(db)

cursor = db.cursor()
try:
    cursor.execute('''
    CREATE TABLE people(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT,
                       phone TEXT, email TEXT , password TEXT)
                   ''')
except sqlite3.OperationalError:
    pass

name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
# A very secure password
password1 = '12345'

name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

# Insert user 1
cursor.execute('''INSERT INTO people(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1, phone1, email1, password1))
print('First user inserted')

# Insert user 2
cursor.execute('''INSERT INTO people(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2, phone2, email2, password2))
print('Second user inserted')

user_id = 2
cursor.execute('''SELECT name, email, phone FROM people WHERE id=?''', (user_id,))
user = cursor.fetchone()
print(user[0])


# -- row factory
db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute('''SELECT name, email, phone FROM people''')
for row in cursor:
    # row['name'] returns the name column in the query, row['email'] returns email column.
    print('{0} : {1}, {2}'.format(row['name'], row['email'], row['phone']))



db.commit()
db.close()