import mysql.connector 

# Initialize database connection
# run this code when running database.py for the first time
# then after first run, coment out code from line 7 - 11, and uncomment 13-20.
'''
db = mysql.connector.connect(
    host="localhost",
    user="root", 
    passwd="password",
)
'''
# durnig second run, the uncommented code will connect to database and populate the tables 

db = mysql.connector.connect(
    host="localhost",
    user="root", 
    passwd="password",
    database="Presentation"
)
mycursor = db.cursor()


# check if database already exists before attempting to create
mycursor.execute("CREATE DATABASE IF NOT EXISTS Presentation")

# Create the Author table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Author (
    author_id int PRIMARY KEY AUTO_INCREMENT,
    author_name VARCHAR(50) NOT NULL)
''')

# Create the Book table with foreign key constraint
# 0 on is_checked means book is is available 
# availability
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Book (
        book_id INT PRIMARY KEY AUTO_INCREMENT,
        book_title VARCHAR(50) NOT NULL,
        publish_year INT NOT NULL, 
        times_checked_out INT NOT NULL, 
        is_checked INT NOT NULL,
        author_id INT, 
        FOREIGN KEY (author_id) REFERENCES Author(author_id)
    )
''')

# Create the Librarian table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Librarian (
        librarian_id INT PRIMARY KEY AUTO_INCREMENT,
        librarian_name VARCHAR(50) NOT NULL,
        book_id INT, 
        FOREIGN KEY (book_id) REFERENCES Book(book_id)
    )
''')

# Create the Vendor table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendor (
        vendor_name VARCHAR(50) NOT NULL,
        book_id INT, 
        FOREIGN KEY (book_id) REFERENCES Book(book_id)
    )
''')

# Create the Patron table with auto-increment primary key
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Patron (
        patron_id INT PRIMARY KEY AUTO_INCREMENT,
        patron_name VARCHAR(50) NOT NULL
    )
''')

# Create the Patron address table with foreign key
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS PatronAddress (
        patron_address_id INT PRIMARY KEY AUTO_INCREMENT,
        patron_id INT,
        street VARCHAR(50) NOT NULL,
        city VARCHAR(50) NOT NULL, 
        state VARCHAR(50) NOT NULL, 
        FOREIGN KEY (patron_id) REFERENCES Patron(patron_id)
    )
''')
# Create the Transaction table
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Transaction (
        transaction_id INT PRIMARY KEY AUTO_INCREMENT, 
        librarian_id INT, 
        book_id INT, 
        patron_id INT, 
        FOREIGN KEY (librarian_id) REFERENCES Librarian(librarian_id), 
        FOREIGN KEY (book_id) REFERENCES Book(book_id), 
        FOREIGN KEY (patron_id) REFERENCES Patron(patron_id)
    )
''')

# Create the TransactionRecord table to handle record details during transactions
mycursor.execute('''
    CREATE TABLE IF NOT EXISTS TransactionRecord (
        record_id INT PRIMARY KEY AUTO_INCREMENT, 
        date_issue DATETIME, 
        date_return DATETIME, 
        transaction_id INT, 
        FOREIGN KEY (transaction_id) REFERENCES Transaction(transaction_id)
    )
''')
db.commit()

# Populate the Author table
author_data = [
    ("Jane Austen",),
    ("Charles Dickens",),
    ("J.K. Rowling",),
    ("Mark Twain",),
    ("William Shakespeare",)
]

sql_author = "INSERT INTO Author (author_name) VALUES (%s)"
mycursor.executemany(sql_author, author_data)
db.commit()

# Populate the Book table
book_data = [
    ("Pride and Prejudice", 1813, 10, 0, 1),
    ("Great Expectations", 1861, 8, 0, 2),
    ("Harry Potter and the Philosopher's Stone", 1997, 15, 0, 3),
    ("The Adventures of Tom Sawyer", 1876, 5, 0, 4),
    ("Romeo and Juliet", 1597, 12, 0, 5)
]

sql_book = "INSERT INTO Book (book_title, publish_year, times_checked_out, is_checked, author_id) VALUES (%s, %s, %s, %s, %s)"
mycursor.executemany(sql_book, book_data)
db.commit()

# Populate the Librarian table
librarian_data = [
    ("John Smith", 1),
    ("Emma Johnson", 2),
    ("Michael Williams", 3)
]

sql_librarian = "INSERT INTO Librarian (librarian_name, book_id) VALUES (%s, %s)"
mycursor.executemany(sql_librarian, librarian_data)
db.commit()

# Populate the Vendor table
vendor_data = [
    ("Book Supplier A", 2),
    ("Book Supplier B", 4),
    ("Book Supplier C", 5)
]

sql_vendor = "INSERT INTO Vendor (vendor_name, book_id) VALUES (%s, %s)"
mycursor.executemany(sql_vendor, vendor_data)
db.commit()

# Populate the Patron table
patron_data = [
    ("Alice Smith",),
    ("Bob Johnson",),
    ("Charlie Williams",)
]

sql_patron = "INSERT INTO Patron (patron_name) VALUES (%s)"
mycursor.executemany(sql_patron, patron_data)
db.commit()

# Populate the PatronAddress table
patron_address_data = [
    (1, "123 Main St", "Cityville", "State A"),
    (2, "456 Elm St", "Townsville", "State B"),
    (3, "789 Oak St", "Villagetown", "State C")
]

sql_patron_address = "INSERT INTO PatronAddress (patron_id, street, city, state) VALUES (%s, %s, %s, %s)"
mycursor.executemany(sql_patron_address, patron_address_data)
db.commit()

# Populating the transaction data and transaction record happen in the functions

db.close()

