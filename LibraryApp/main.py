#import function for running main functions
from library_app import search_books_with_input, check_out_book_with_input, return_book_with_input

# separate the running functions from main into function place holder to easily create a while loop 
# for users to endlessly use application 
def run(): 
    search_books_with_input()

    check_out_book_with_input()

    return_book_with_input()
        

if __name__ == "__main__":
    
    #run the application 
    run()
    
    #continue or quit
    repeat = True
    while repeat: 
        #continue/repeat the application 
        conApp = input("Would you like to leave the library? (y/n)")
        try: 
            if(conApp.lower() == 'y'): 
                repeat = False
                break
            elif(conApp.lower() == 'n'): 
                run()
        except ValueError: 
            print("Please enter y to leave, or n to stay. Please try again!")
            