### Short description of program.
"""
Book store application using a combination of in-memory data structures and external files for storage.
For receiving and processing user input, the program uses an in-memory database system built from dictionaries in a list.
Upon start, the program will also ask the user to use an existing database file or create a new one, which will be continuously
updated as the user performs changes while running the program. 

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
- (Optional) Mark a book as read
- (Optional) Do any of the previous steps again
- Quit the program
"""

### Definitions below.
"""
The data structure of the database will be of the following format:
database  = [
    book1 = {
        "title": ... {str},
        "author": ... {str},
        "year": ... {int},
        "pages": ... {int},
        "genre": ... {str},
        "read": ... {bool}
    },
    book2 = {...},
    book3 = {...}
]
"""

### Features/goals.
"""
[X]: How do we store the books? - in-memory and as JSON files
[X]: Quit program when user types "q"
[X]: Add function for adding book to database
[X]: Add function for listing all books in the database
[X]: Add function for finding / searching for book(s) in the database
[X]: Add function for marking a book as read
[X]: Add function for deleting a book from the database
[X]: Add function for reading database from JSON file
[X]: Add function for saving/writing database from JSON file
"""

### Import modules.
from utils import database
import os

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
def menu(database_con, table_name):
    """
    Menu function that deals with user interaction, input, and exiting the program.
    Calls other functions that deal with interacting with the database.
    """

    while True:
        # Get number of rows in the table.
        cursor = database_con.cursor()
        n_rows = cursor.execute(f"SELECT COUNT(*) FROM books").fetchone()[0]

        user_input = input(choice_message)

        if user_input.lower() in ["a", "add"]:
            database.add_book(database_con)
        elif user_input.lower() in ["q", "quit"]:
            break
        elif n_rows > 0:
            if user_input.lower() in ["l", "list"]:
                database.list_books(database_con)
            elif user_input.lower() in ["f", "find", "s", "search"]:
                database.find_books(database_con)
            elif user_input.lower() in ["r", "read"]:
                database.mark_books(database_con)
            elif user_input.lower() in ["d", "delete"]:
                database.delete_books(database_con)
            else:
                print("\nYou did not type one of the options, please try again.\n")
        else:
            print("\nPlease add a book or exit the program.\n")


# Run program.
if __name__ == "__main__":
    print(
"""
Welcome to the book database program!
NB:This program uses SQLite for the database.
"""
    )
    
    database_con, table_name = database.create_database_table()

    menu(database_con, table_name)

    cursor = database_con.cursor()
    n_rows = cursor.execute(f"SELECT COUNT(*) FROM books").fetchone()[0]

    print("Stopping the book database program ...")
    print("\nFinal book database content:")
    if n_rows > 0:
        database.list_books(database_con)
        #database.write_database(book_database, database_name)
        database_con.commit()
    else:
        print("No data to save.")
    
    database_con.close()
    print("Done!\nSee ya :)\n")
