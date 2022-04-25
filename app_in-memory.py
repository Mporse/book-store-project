"""
Book store application using only in-memory data structures.
"""

### Features/goals:
# [X] Quit program when user types "q"
# [] Add function for adding book to database
# [] (related to above) Set up database system that the code should interact with
# [] Add function for listing all books in the database
# [] Add function for marking a book as read
# [] Add function for deleting a book from the database
# [] Add error handling (for dealing with weird inputs from user)


# Import modules.
from utils import database

# Define message for users to make a choice.
choice_message = """List of choices:
- "a" (for adding a book to the database)
- "l" (to list all the books in the database)
- "r" (to mark a book as read)
- "d" (to delete a book from the database)
- "q" (to quit the program)

Type your choice here: """


def menu():
    user_input = input(choice_message)
