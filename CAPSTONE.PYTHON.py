import sqlite3

db = sqlite3.connect('finance.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS finance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    amount REAL,
    category TEXT,
    type TEXT
)
''')

db.commit()

name = input('Enter income name: ')
amount = float(input('Enter amount: '))
category = input('Enter category: ')

cursor.execute('''
INSERT INTO finance (name, amount, category, type)
VALUES (?, ?, ?, ?)
''', (name, amount, category, 'Income'))

db.commit()

print('Income added successfully!')

db.close()
