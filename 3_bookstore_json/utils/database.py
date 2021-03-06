"""
This is a movie database/storage program.
The program uses built-in Python data structures when working with user inputs,
but contains the ability to save and load the database to/from JSON files as well.
"""

import json

def add_book(book_database):
    """
    Function that adds a new book to the database.
    Asks for user input regarding book title, author, release year, number of pages, and genre.
    """

    book_title = input("Type the title of the book: ")
    book_author = input("Type the author of the book: ")
    book_year = input("Type the release year of the book: ")
    book_pages = input("Type the number of pages in the book: ")
    book_genre = input("Type the genre of the book: ")
    book_read = False

    book_database.append({"title": book_title,
                          "author": book_author,
                          "year": book_year,
                          "pages": book_pages,
                          "genre": book_genre,
                          "read": book_read})
    
    print("\nBook added!\n")
    print(f"Title: {book_title}")
    print(f"Author: {book_author}")
    print(f"Release year: {book_year}")
    print(f"Pages: {book_pages}")
    print(f"Genre: {book_genre}")
    print(f"Read: {book_read}\n")


def list_books(book_database):
    """
    Function that lists all the books added to the database.
    """

    for book in book_database:
        print("")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Release year: {book['year']}")
        print(f"Pages: {book['pages']}")
        print(f"Genre: {book['genre']}")
        print(f"Read: {book['read']}")
    print()


def find_books(book_database):
    """
    Function used to search through the database and find matching entries,
    then returning the found entries.
    """

    properties = list(book_database[0].keys())[0:-1]
    properties_to_select = "\n- ".join(properties)

    print(f"Properties:\n- {properties_to_select}\n")

    while True:
        selected_property = input("Type which property from above you want to use for searching for books: ")

        if selected_property.lower() not in properties:
            print("You did not type one of the listed properties. Try again.")
        else:
            break

    search_term = input("Type the search term: ")
    list_property = [book[selected_property.lower()] for book in book_database]
    found_books = [search_term.lower() == prop.lower() for prop in list_property]
    found_books = [idx for idx, term_bool in enumerate(found_books) if term_bool]
    output = [book_database[idx] for idx in found_books]

    list_books(output)


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
