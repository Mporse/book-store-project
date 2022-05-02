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
    pass


def mark_books(book_database):
    pass


def delete_books():
    pass

