from Book import Book
class Member:
    def __init__(self, Member_ID, Name, Email):
        self.Member_ID = Member_ID
        self.Name = Name
        self.Email = Email
        self.Borrowed_Books = []

    def Borrow_Books(self, book):
        "Borrow a Book from the Library if the Specific book is available"
        if book.Check_Availability():
            self.Borrowed_Books.append(book)
            book.Update_Quantity(-1)
            print(f"{self.Name},'{book.Title}'")
        else:
                print (f"Sorry, '{book.Title}' is not available")

    def Return_Book(self, Book):
        " Return a Book to the Library."
        if Book in self.Borrowed_Books:
            self.Borrowed_Books.remove(Book)
            Book.Update_Quantity(1)
            print(f"{self.Name} does not have the '{Book.Title}'")

    def view_Borrowed_Books(self):
        "View the list of borrowed books by the Member."
        if self.Borrowed_Books:
            print(f"{self.Name} Borrowed_Books:")
            for Book in self.Borrowed_Books:
                print(f" -{Book.Title}")

        else:
            print(f"{self.Name} has not borrowed any book.")

if __name__ == "__main__":
   M1 = Member('001',"Purav Satish","purav@gmail.com")
   b1 = Book('003',"Think and Grow Rich","Napoleon Hill",1)
   M1.Borrow_Books(b1)
   M1.view_Borrowed_Books()
