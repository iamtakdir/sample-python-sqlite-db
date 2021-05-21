import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory= sqlite3.Row

def create_table():
    with connection:
        connection.execute("Create table if not exists entries  (note TEXT ,date TEXT);")

def add_entry(entry_note,entry_date):
    with connection:
        connection.execute("Insert into entries Values (?,?);", (entry_note, entry_date))


def get_entry():
  
    cursor = connection.execute("select * from entries; ")
    return cursor
