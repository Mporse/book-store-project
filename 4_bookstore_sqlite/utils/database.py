"""
This is a book store database/storage program.
The program uses built-in Python data structures when working with user inputs,
but contains the ability to save and load the database via SQLite.
"""

import os
import sqlite3

def create_database_table(database_folder = "./database_files"):
    """
    Function to create the database and table for storing book information.
    """

    # Create folder for storing database files if it doesn't already exist.
    if not os.path.exists(database_folder):
        os.makedirs(database_folder)
    
    # Get the names of the databases in the folder.
    databases_in_folder = [file_name[:-3] for file_name in os.listdir(database_folder)]
    databases_in_folder_all = "\n- ".join(databases_in_folder)

    while True:
        database_name = input(
f"""
Any existing tables in the database are displayed below:
- {databases_in_folder_all}


Type the name of the table you wish to select, or type a new name to create a new table:
""").lower()
        
        if not database_name:
            print("Please enter a valid table name.\n")
            continue
        break # end of while loop

    # Connect to "data" database.
    database_con = sqlite3.connect(f"{database_folder}/{database_name}.db")
    cursor = database_con.cursor()

    if database_name in databases_in_folder:
        print(f"You selected database {database_name} ... ")
    else:
        print(f"Creating database {database_name} ... ")
        cursor.execute(
f"""CREATE TABLE books (
    title VARCHAR(200) PRIMARY KEY,
    author VARCHAR(100),
    year INT,
    pages INT,
    genre VARCHAR(50),
    read BOOLEAN
)""")

    database_con.commit()

    return database_con, database_name


def fetch_one_helper(book_data):
    print()
    print(f"Title: {book_data[0]}")
    print(f"Author: {book_data[1]}")
    print(f"Release year: {book_data[2]}")
    print(f"Pages: {book_data[3]}")
    print(f"Genre: {book_data[4]}")
    print(f"Read: {'false' if book_data[5] == 0 else 'true'}")


def add_book(database_con):
    """
    Function that adds a new book to the database.
    Asks for user input regarding book title, author, release year, number of pages, and genre.
    """

    book_title = input("Type the title of the book: ").lower()
    book_author = input("Type the author of the book: ").lower()
    book_year = input("Type the release year of the book: ")
    book_pages = input("Type the number of pages in the book: ")
    book_genre = input("Type the genre of the book: ").lower()
    book_read = False

    cursor = database_con.cursor()
    cursor.execute(
        f"INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)",
        (book_title, book_author, book_year, book_pages, book_genre, book_read)
        )
    
    database_con.commit()

    book_data = (book_title, book_author, book_year, book_pages, book_genre, book_read)

    fetch_one_helper(book_data)


def list_books(database_con):
    """
    Function that lists all the books added to the database.
    """

    cursor = database_con.cursor()
    cursor.execute("SELECT * FROM books")

    while True:
        try:
            book_data = list(cursor.fetchone())
            fetch_one_helper(book_data)
        except:
            break


def find_books(database_con):
    """
    Function used to search through the database and find matching entries,
    then returning the found entries.
    """

    cursor = database_con.cursor()

    # Get all properties (column names) of table.
    cursor.execute("SELECT name FROM PRAGMA_TABLE_INFO('books')")
    properties = [col_name[0] for col_name in cursor.fetchall()]
    properties_to_select = "\n- ".join(properties)

    print(f"Properties:\n- {properties_to_select}\n")

    while True:
        selected_property = input("Type which property from above you want to use for searching for books: ").lower()

        if selected_property not in properties:
            print("You did not type one of the listed properties. Try again.")
        else:
            break

    search_term = input("Type the search term: ").lower()

    if selected_property == "read":
        if search_term == "true":
            search_term = 1
        elif search_term == "false":
            search_term = 0

    cursor.execute(f"SELECT * FROM books WHERE {selected_property} = ?", (search_term,))

    i = 0

    while True:
        try:
            book_data = list(cursor.fetchone())
            fetch_one_helper(book_data)
        except TypeError:
            break
        i += 1

    print("\nNo book found!") if i == 0 else print()


def mark_books(book_database):
    """
    Function to mark a book as read.
    """

    user_input = input("Type the title of the book you wish to mark as read: ")

    for book_idx in range(len(book_database)):
        if user_input.lower() == book_database[book_idx]["title"].lower():
            book_database[book_idx]["read"] = True
            print(f"Marked book as read: \"{book_database[book_idx]['title']}\"")


def delete_books(book_database):
    """
    Function for deleting a user-specifid book from the database.
    """

    user_input = input("Type the title of the book you wish to delete: ")

    while True:
        for book_idx in range(len(book_database)):
            if user_input.lower() == book_database[book_idx]["title"].lower():
                deleted_book = book_database.pop(book_idx)
                print(f"Deleted book: \"{deleted_book['title']}\"")
                break
        break


def read_database(database_name):
    """
    Function to read database data from a JSON file.
    """

    with open(f"./database_files/{database_name}.json", "r") as book_database_file:
        print("Database found - loading ...")
        
        book_database = json.load(book_database_file)
        
        print("Database loaded!\n")
    
    return book_database


def write_database(book_database, database_name):
    """
    Function to write database data to a JSON file.
    """

    with open(f"./database_files/{database_name}.json", "w") as book_database_file:
        print("Saving database ...")
        
        json.dump(book_database, book_database_file, indent=4)

        print("Database saved!\n")
