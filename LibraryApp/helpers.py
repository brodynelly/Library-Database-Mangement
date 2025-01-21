from sql_queries import connect_to_database
import mysql.connector

# Function to get a list of authors from the database
def get_authors():
    db = connect_to_database()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT author_id, author_name FROM Author") #SQL queruie selecting authors in the database
            authors = cursor.fetchall()
            return authors
        except mysql.connector.Error as err:
            print(f"Error executing SQL query: {err}")
        finally:
            db.close()
    return None

# Function to get book that have not been checked out
def get_available_books():
    db = connect_to_database()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT book_id, book_title FROM Book WHERE is_checked < 1") # selects books from table BOOK that have not been checked out 
            available_books = cursor.fetchall()
            return available_books
        except mysql.connector.Error as err:
            print(f"Error executing SQL query: {err}")
        finally:
            db.close()
    return None

# Function to get a list of patrons who have borrowed a specific book from the database
def get_patrons_with_book(book_id):
    db = connect_to_database()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute(f"SELECT Patron.patron_id, patron_name FROM Patron JOIN Transaction ON Patron.patron_id = Transaction.patron_id WHERE Transaction.book_id = {book_id}")
            patrons_with_book = cursor.fetchall()
            return patrons_with_book
        except mysql.connector.Error as err:
            print(f"Error executing SQL query: {err}")
        finally:
            db.close()
    return None

# Function to get a list of patrons from the database
def get_patrons():
    db = connect_to_database()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT patron_id, patron_name FROM Patron")
            patrons = cursor.fetchall()
            return patrons
        except mysql.connector.Error as err:
            print(f"Error executing SQL query: {err}")
        finally:
            db.close()
    return None

# Function to return a list of selected books that have been checked out from the library
def get_borrowed_books():
    db = connect_to_database()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT Book.book_id, book_title, author_name FROM Book JOIN Author ON Book.author_id = Author.author_id WHERE is_checked > 0")
            borrowed_books = cursor.fetchall()
            return borrowed_books
        except mysql.connector.Error as err:
            print(f"Error executing SQL query: {err}")
        finally:
            db.close()
    return None
