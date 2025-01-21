import mysql.connector

# Function to connect connect the library application to the created MySQL database
def connect_to_database():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="password",
            database="libtest2"
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None
    
# Function to search for books based on criteria
def search_books(search_criteria):
    db = connect_to_database()
    if db:
        # try-execpt-finally statement to handle fail cases of database not connecting correctly 
        try:
            cursor = db.cursor()
            query = f"SELECT Book.book_id, book_title, author_name, publish_year, times_checked_out FROM Book JOIN Author ON Book.author_id = Author.author_id WHERE {search_criteria}"
            cursor.execute(query)
            books = cursor.fetchall()
            #displays the matching book based on returning SQL queury from the database (passed as parameter in function) 
            if books:
                print("\nMatching Books:")
                print("(book_id, book_title, author_name, publish_year, times_checked_out)")
                for book in books:
                    print(book)
            else:
                print("No books found for the selected author.")
        except mysql.connector.Error as err:
            print(f"Error executing SQL query: {err}")
        finally:
            db.close()

# Function to check out a book
def check_out_book(patron_id, book_id):
    db = connect_to_database()
    if db:
        # try-execpt-finally statement to handle fail cases of database not connecting correctly
        try:
            cursor = db.cursor()
            # Check if the book is available
            cursor.execute(f"SELECT book_title, is_checked, times_checked_out FROM Book WHERE book_id = {book_id}")
            book_data = cursor.fetchone()
            if book_data:
                book_title, is_checked, times_checked_out = book_data
                #updates tables accordingly for user to checkout book after selecting from SQL queuery 
                if is_checked == 0:
                    print(f"{book_title} is available for checkout.")
                    # Reserve the book for the patron by updating its status to "borrowed"
                    cursor.execute(f"UPDATE Book SET times_checked_out = times_checked_out + 1, is_checked = 1 WHERE book_id = {book_id}")
                    db.commit()
                    # Create a transaction record linking the patron, book, and transaction details
                    cursor.execute(f"INSERT INTO Transaction (librarian_id, book_id, patron_id) VALUES (1, {book_id}, {patron_id})")
                    db.commit()
                    
                    print("Book checked out successfully.")
                else:
                    print(f"{book_title} is not available for checkout.")
            else:
                print("Book not found.")
        except mysql.connector.Error as err:
            print(f"Error executing SQL query: {err}")
        finally:
            db.close()
            
            
# Function to return a book to the library
def return_book(patron_id, book_id):
    db = connect_to_database()
    # try-execpt-finally statement to handle fail cases of database not connecting correctly 
    if db:
        try:
            cursor = db.cursor()
            # Check if the book is borrowed by the specified patron
            cursor.execute(f"SELECT Book.book_title, Transaction.patron_id, Book.is_checked FROM Transaction JOIN Book ON Transaction.book_id = Book.book_id WHERE Transaction.book_id = {book_id} AND Transaction.patron_id = {patron_id}")
            transaction_data = cursor.fetchone()  # Fetch the result
            if transaction_data:
                book_title, retrieved_patron_id, is_checked = transaction_data
                if retrieved_patron_id == patron_id:
                    
                    if is_checked > 0:  # Check if the book is checked out
                        print(f"\n{book_title} has been successfully returned by the specified patron.")
                        # Update book status to "available"
                        cursor.execute(f"UPDATE Book SET is_checked = 0 WHERE book_id = {book_id}")
                        db.commit()
                    
                        print("Book returned successfully.")
                    else:
                        print("Book is already available.")
                else:
                    print("Book is not borrowed by the specified patron.")
            else:
                print("Book is not borrowed by the specified patron.")
        except mysql.connector.Error as err:
            print(f"Error executing SQL query: {err}")
        finally:
            db.close()