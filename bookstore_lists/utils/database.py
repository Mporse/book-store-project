"""
Script/module with functions for interacting with database.
There are functions defineded for dealing with adding, deleting, listing and marking books as read.
Other helper function might also have been defined (TBD).
"""

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

    book_database.append({"title": book_title,
                          "author": book_author,
                          "year": book_year,
                          "pages": book_pages,
                          "genre": book_genre})
    
    print("\nBook added!\n")
    print(f"Title: {book_title}")
    print(f"Author: {book_author}")
    print(f"Release year: {book_year}")
    print(f"Pages: {book_pages}")
    print(f"Genre: {book_genre}\n")


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
    
    print()


def find_books(book_database):
    """
    Function used to search through the database and find matching entries,
    then returning the found entries.
    """

    properties_to_select = "\n- ".join(book_database[0].keys())

    print(f"Properties:\n- {properties_to_select}\n")

    while True:
        selected_property = input("Type which property from above you want to use for searching for books: ")

        if selected_property.lower() not in book_database[0].keys():
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
    pass


def delete_books():
    pass

