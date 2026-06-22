class Book:
    def __init__(self, Book_ID, Title, Author, Quantity):
        self.Book_ID = Book_ID
        self.Title = Title
        self.Author = Author
        self.Quantity = Quantity


    def display_Book_Information(self):
        "Display the Book's Information (Book_ID, Title, Author, Quantity)"
        print (f"ID:{self.Book_ID}, Title:{self.Title}, Author:{self.Author}, Quantity:{self.Quantity}")

    def Check_Availability(self):
        " Check if the book is Available (Quantity > 0)."
        return self.Quantity > 0

    def Update_Quantity(self, quantity):
        " Update the Quantity of the book (Borrow or Return) "
        self.Quantity += quantity
        
if __name__ == "__main__":
    b1 = Book('001', "Rich Dad,Poor Dad","Robert Kiyosaki & Sharon Lechter",5)
    b2 = Book('002',"Never split the difference" ,"Christopher Voss & Tahl raz", 3)
    b3 = Book('003',"Think an Grow Rich","Napoleon Hill",1)
    b4 = Book('004',"The innovato's Dilemma","Clayton ChrisTenSen",4)
    b5 = Book('005',"Zero to One","Blake Masters & Peter Thiel",3)
    b6 = Book('006',"The Art of war","Sun tzu",2)
    b7 = Book('007',"Good to Great","Jim Collins",3)
    b1.display_Book_Information()
    b2.display_Book_Information()
    b3.display_Book_Information()
    b4.display_Book_Information()
    b5.display_Book_Information()
    b6.display_Book_Information()
    b7.display_Book_Information()
    print(b1.Check_Availability())
    b1.Update_Quantity(-1)
    print(b1.Quantity)
