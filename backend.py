import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, autor text, year INTEGER, isbn INTEGER)")
    
    conn.commit()
    conn.close()


def insert(title, autor, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, autor, year, isbn))
    conn.commit()
    conn.close()
    
    
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor() 
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title= "", autor= "", year= "", isbn= ""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor() 
    cur.execute("SELECT * FROM book WHERE title= ? OR autor= ? OR year= ? OR isbn= ?", (title, autor, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor() 
    cur.execute("DELETE FROM book WHERE id= ?", (id,))
    conn.close()
    
    
def delete(id, title, autor, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor() 
    cur.execute("UPDATE book SET title= ?, autor= ?, year= ?, isbn= ?",(title, autor, year, isbn, id))
    conn.close()


connect()
# insert("python ebook", "ali", 2018, 4389)
print(view())
