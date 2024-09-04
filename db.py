import sqlite3
from enum import member

from setup_db import cursor


def connect_db():
    conn = sqlite3.connect('lib.db')
    cursor = conn.cursor()
    return conn, cursor

def add_book(title, author, copies):
    conn, cursor = connect_db()
    cursor.execute('''
        INSERT INTO books (title, author, copies)
        VALUES (?, ?, ?)
    ''',(title, author, copies))
    conn.commit()
    conn.close()
    print(f"Book '{title}' by {author} added with {copies} copies.")

def delete_book(book_id):
    conn, cursor = connect_db()
    cursor.execute('DELETE FROM books WHERE id = ?',(book_id,))
    conn.commit()
    conn.close()
    print(f"Book with ID {book_id} deleted.")

def view_books():
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()

    if books:
        print("\nList of Books")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Copies Available: {book[3]}")
    else:
        print("No books available in the library.")

def add_members(name, email):
    conn, cursor = connect_db()
    try:
        cursor.execute('''
            INSERT INTO members(name,email)
            VALUES (?, ?)
        ''', (name, email))
        conn.commit()
        print(f"Member '{name}' added with email '{email}'.")
    except sqlite3.IntegrityError:
        print("Error: A member with this email already exists.")
    finally:
        conn.close()

def view_members():
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM members')
    members = cursor.fetchall()
    conn.close()

    if members:
        print("\nList of Members:")
        for member in members:
            print(f"ID: {member[0]}, Name: {member[1]}, Email: {member[2]}")
    else:
        print("No members available.")

def delete_member(mem_id):
    conn, cursor = connect_db()
    cursor.execute('DELETE FROM members WHERE id = ?',(mem_id,))
    conn.commit()
    conn.close()
    print(f"Member with ID {mem_id} deleted.")

















