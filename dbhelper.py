import os.path
import sqlite3
from posel import Posel

def connect_db():
    try:
        conn = sqlite3.connect('sejm.db')
    except:
        print("wystąpił błąd w połączeniu się z bazą danych")
        conn = None
    finally:
        return conn

def create_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS poslowie (
        posel_id INTEGER PRIMARY KEY ,
        nazwa TEXT NOT NULL,
        partia TEXT NOT NULL,
        wyksztalcenie TEXT,
        szkola TEXT,
        zawod TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

def insert_posel_into_db(posel: Posel):
    conn = connect_db()
    cur = conn.cursor()
    sql = '''
    INSERT INTO poslowie(nazwa, partia, wyksztalcenie, szkola, zawod)
    VALUES(?,?,?,?,?);
    '''
    cur.execute(sql, posel.obj_into_tuple())
    conn.commit()
    conn.close()