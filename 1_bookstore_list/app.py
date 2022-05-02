### Short description of program.
"""
Book store application using only in-memory data structures.

These should be the options for the user when running the program:
- Enter 'a' to add a book to the database
- Enter 'l' to list the books in the database
- Enter 'f' to find a book in the database
- Enter 'r' to mark a book as read
- Enter 'd' to delete a book from the database
- Enter 'q' to quit the program

The workflow of using the program should be as follows:
- Add book
- See book(s)
- Find a book
- (Optinal) Mark a book as read
- (Optional) Do any of the previous steps again
- Quit the program
"""

### Definitions below.
"""
The data structure of the movie will be of the following format:
movie = {
    "title": ... {str},
    "director": ... {str},
    "year": ... {int},
    "duration": ... {int},
    "genre": ... {str},
    "cast": ... {list}{str},
    
}
"""

### Features/goals.
"""
[X]: How do we store the movies? - in-memory
[X]: Quit program when user types "q"
[X]: Add function for adding book to database
[X]: Add function for listing all books in the database
[X]: Add function for searching for book(s) in the database
[X]: Add function for marking a book as read
[X]: Add function for deleting a book from the database
"""

### Import modules.
from utils import database

### Main part of the program.
# Define message for users to make a choice.
choice_message = """
Choices to select from:
- 'a' (for adding a book to the database)
- 'l' (to list all the books in the database)
- 'f' (to find/search for a book in the database)
- 'r' (to mark a book as read)
- 'd' (to delete a book from the database)
- 'q' (to quit the program)

Type your choice here: """

# Define menu function.
def menu(book_database):
    """
    Menu function that deals with user interaction, input, and exiting the program.
    Calls other functions that deal with interacting with the database.
    """
    
    while True:
        user_input = input(choice_message)

        if user_input.lower() in ["a", "add"]:
            database.add_book(book_database)
        elif user_input.lower() in ["q", "quit"]:
            break
        elif len(book_database) > 0:
            if user_input.lower() in ["l", "list"]:
                database.list_books(book_database)
            elif user_input.lower() in ["f", "find", "s", "search"]:
                database.find_books(book_database)
            elif user_input.lower() in ["r", "read"]:
                database.mark_books(book_database)
            elif user_input.lower() in ["d", "delete"]:
                database.delete_books(book_database)
            else:
                print("\nYou did not type one of the options, please try again.\n")
        else:
            print("\nPlease add a book or exit the program.\n")

# Run program.
if __name__ == "__main__":
    print(
"""
Welcome to the book database program!
NB:This program uses Python lists (in-memory data structures) for the database, so nothing is saved when the program exits.
"""
    )

    book_database = []

    menu(book_database)

    print("Stopping the book database program ...")
    print("\nFinal book database content:")
    if len(book_database) > 0:
        database.list_books(book_database)
    else:
        print("No data.")
