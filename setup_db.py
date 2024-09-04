import sqlite3

conn = sqlite3.connect('lib.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,  
        copies INTEGER NOT NULL DEFAULT 1 -- Default to 1 copy available
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS members(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS loans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        mem_id INTEGER NIT NULL,
        loan_date TEXT NOT NULL,
        return_date TEXT,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (mem_id) REFERENCES members(id)
    )
''')

conn.commit()
conn.close()

print("Database created Successfully!")