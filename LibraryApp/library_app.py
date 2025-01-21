#imports from helper python files
from datetime import datetime
from helpers import get_authors, get_available_books, get_patrons_with_book, get_patrons, get_borrowed_books
from sql_queries import search_books, check_out_book, return_book

# Function A: Search for Specific Books with user input for author selection
def search_books_with_input():
    authors = get_authors()
    # check if authors exists 
    if authors:
        #displays all the authors, and prompts user to select author
        print("Select an author to search for books:")
        for author in authors:
            print(f"{author[0]}. {author[1]}")
        author_choice = input("Enter the number corresponding to the author: ")
        
        # checks selected author for fail cases and invalid SQL results 
        try:
            author_id = int(author_choice)
            if author_id not in [author[0] for author in authors]:
                print("Invalid author selection.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        # search for authors work based on user input 
        search_criteria = f"Book.author_id = {author_id}"  
        search_books(search_criteria)
    else:
        print("No authors found in the database.")
        


# Function B: Check Out Books with user input for patron ID and book ID
def check_out_book_with_input():
    # Get list of available books
    available_books = get_available_books()
    if not available_books:
        print("No available books.")
        return

    # Display available books
    print("\nPlease Select an Available Book to Check Out:")
    for book in available_books:
        print(f"{book[0]}. {book[1]}")

    # Prompt user to select a book
    book_choice = input("Enter the number corresponding to the book to check out: ")

    try:
        book_id = int(book_choice)
        if book_id not in [book[0] for book in available_books]:
            print("Invalid book selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Get list of patrons
    patrons = get_patrons()
    if not patrons:
        print("No patrons found.")
        return

    # Display available patrons
    print("\n Which Patron are You?:")
    for patron in patrons:
        print(f"{patron[0]}. {patron[1]}")

    # Prompt user to select a patron
    patron_choice = input("Enter the number corresponding to the patron to check out the book: ")

    try:
        patron_id = int(patron_choice)
        if patron_id not in [patron[0] for patron in patrons]:
            print("Invalid patron selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Proceed to check out the selected book by the selected patron
    check_out_book(patron_id, book_id)
    
# Function C: Return Books to the Library with user input for patron and book selection
def return_book_with_input():
    # Get list of borrowed books
    borrowed_books = get_borrowed_books()
    if not borrowed_books:
        print("No borrowed books.")
        return
    
    #ask if patron would like to return book 
    return_book_question = input("\nwould you like to return a book?(y/n): ")
    if return_book_question.lower() == "y":
        print("Continuing...")
    elif return_book_question.lower() == "n":
        print("Exiting...")
        return
    else:
        print("Invalid input. Please enter 'y' for Yes or 'n' for No.")
        
    
    
    # Display patrons who borrowed the book
    print("\nPlease select which patron you are:")
    for patron in get_patrons():
        print(f"{patron[0]}. {patron[1]}")

    # Prompt user to select the patron who is returning the book
    patron_choice = input("enter the number coorasponding to your name: ")

    # Display borrowed books
    print("\nList of Borrowed Books:")
    for book in borrowed_books:
        print(f"{book[0]}. {book[1]}")

    # Prompt user to select a book to return
    book_choice = input("Enter the number corresponding to the book to return: ")

    try:
        book_id = int(book_choice)
        if book_id not in [book[0] for book in borrowed_books]:
            print("Invalid book selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Get list of patrons who borrowed the selected book
    patrons_with_book = get_patrons_with_book(book_id)
    if not patrons_with_book:
        print("\nNo patrons found who borrowed this book.")
        return

    try:
        patron_id = int(patron_choice)
        if patron_id not in [patron[0] for patron in patrons_with_book]:
            print("\nYou have not checked out the selected book!")
            print("You are currently only able to return books you have checked out :(")
            return
    except ValueError:
        print("\n1Invalid input. Please enter a number.")
        return

    # Proceed to return the selected book by the selected patron
    return_book(patron_id, book_id)



