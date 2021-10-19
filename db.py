import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect("db.sqlite")

Cursor = conn.cursor()
sql_query = """ CREATE TABLE user (
    id integer PRIMARY KEY,
    email text NOT NULL UNIQUE,
    password text NOT NULL,
    name text NOT NULL
)"""

Cursor.execute(sql_query)