class Librarian:
    def __init__(self, ID, Name, Designation):
        self.ID = ID
        self.Name = Name
        self.Designation = Designation

    def display_info(self):
        "Display Librarian Details"
        print(f"ID: {self.ID}")
        print(f"Name:{self.Name}")
        print(f"Designation:{self.Designation}")

    def update_designation(self, new_designation):
        "Update librarian designation."
        self.Designation = new_designation
        print("Designation updated sucessfully")

    def add_book(self, Title):
        "Record adding a book"
        print(f"{self.Name} added to the book '{Title}'.")

    def remove_book(self, Title):
        "Record removing a book."
        print(f"{self.Name} removed the book '{Title}'.")

if __name__ == "__main__":
    L1 = Librarian("L001", "Dua Lipa", "Head Librarian")
    L1.display_info()
    L1.update_designation("Senior Librarian")
    L1.display_info()
    L1.add_book("1984")
    L1.remove_book("1984")
