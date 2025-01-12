class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        # Add book to library
        self.books.append(book)
        print(f"({book.title} by {book.author}) added to {self.name} library\n")

    def remove_book(self, book):
        # Find the book with matching title and author
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                self.books.remove(b)
                print(f"({book.title} by {book.author}) was removed from {self.name} library\n")
                return
        print(f"{book.title} by {book.author} is not in {self.name} library\n")

    def search_books(self, search_string):
        # Search through titles and authors (case insensitive) for a match in string
        search_string = search_string.lower()
        book_list = []

        for book in self.books:
            if (search_string in book.title.lower() or
                search_string in book.author.lower()):
                print(f"Found book ({book.title} by {book.author}) matching ({search_string})\n")
                book_list.append(book)
        
        if book_list:
            return book_list
        
        print(f"({search_string}) not in {self.name} library\n")
        return []
