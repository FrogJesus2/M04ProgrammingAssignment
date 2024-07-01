import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE book
             (title TEXT PRIMARY KEY,
             author TEXT,
             year INT)''')

conn.commit()
conn.close()