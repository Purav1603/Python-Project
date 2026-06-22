import csv 
from Book import Book 

class library:
    def __init__(self):
        self.Books = []
        self.Memmbers = []
    
    def Add_Book(self, book):
        "Add a book to the library"
        self.Books.append(book)

    def Search_Book(self, book_ID):
        "Search a Book its ID and display it if the book is found"
        for book in self.Books:
            if book.Book_ID == book_ID:
                book.display_Book_Information()
                return 
        print(f"No Book has been found with ID {book_ID}.")
    
    def Save_Books_To_Csv(self, filepath):
        "Save all books in the library to a CSV file:"
        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["book_ID","Title","Author","Quantity"])
            for book in self.Books:
                writer.writerow([book.Book_ID, book.Title, book.Author, book.Quantity])
    
    def Load_Books_From_Csv(self, filepath):
        "Load books from a CSV file into the library."
        try:
            with open(filepath, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    book = Book (row[0], row[1], row[2], int(row[3]))
                    self.Add_Book(book)
        except FileNotFoundError:
            print(f"The File {filepath} was not found")
                    


if __name__ == "__main__":
    lib = library()
    b1 = Book("001","1984","George Orwell",5)
    lib.Add_Book(b1)
    for book in lib.Books:
        book.display_Book_Information()
    lib.Search_Book("001")
    lib.Search_Book("999")
    lib.Save_Books_To_Csv("test_books.csv")
    lib.Load_Books_From_Csv("test_books.csv")
