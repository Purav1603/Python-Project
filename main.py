from Book import Book
from Member import Member
from Library import library

def main():
    lib = library()
    lib.Load_Books_From_Csv("books.csv")

    while True:
        print("\n--- Library Management System ---")
        print("1. View all books")
        print("2. Add a new book")
        print("3. Search for a book")
        print("4. Save books to file")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            for book in lib.Books:
                book.display_Book_Information()

        elif choice == "2":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))
            new_book = Book(book_id, title, author, quantity)
            lib.Add_Book(new_book)
            print("Book added successfully!")

        elif choice == "3":
            book_id = input("Enter Book ID to search: ")
            lib.Search_Book(book_id)

        elif choice == "4":
            lib.Save_Books_To_Csv("books.csv")
            print("Books saved successfully")

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Not Found, try again.")

if __name__ == "__main__":
    main()
