#Simple Library For Terminal Using OOP

class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
    

class library:
    def __init__(self):
        self.book = []

    def addbook(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book year: ")

        books = book(title, author, year)
        self.book.append(books)
        print(f"Book Added: {books}")

    def viewbook(self):
        if not self.book:
            print("No Books Available!")
        else:
            print("---> Library Books <---")
            for i, book in enumerate(self.book, start=1):
                print(f"{i}. {book}")

    def searchbook(self):
        title = input("Enter book title to search: ")
        book_found = [book for book in self.book if book.title.lower() == title.lower()]

        if book_found:
            print("---> Search Result <---")
            for b in book_found:
                print(b)
        else:
            print("Book not Found!")

    def removebook(self):
        if not self.book:
            print("No Books Available!")
        else:
            self.viewbook()
            try:
                removebook = int(input("Enter number book you want to remove: "))
                if 1 <= removebook <= len(self.book):
                    removed = self.book.pop(removebook - 1)
                    print(f"Book '{removed}' Successfully removed!")
                else:
                    print("Invalid Book Number!")
            except ValueError:
                print("Please Enter Valid Number")

    def exitlibrary(self):
        if not self.book:
            print("Thank You for Using my Simple Library")
            exit()
        


    def run(self):
       while True:
           
           print("1. Add Books")
           print("2. View Books")
           print("3. Search Books")
           print("4. Remove Books")
           print("5. Exit Library")

           choice = input("Enter Number[1-5]: ")

           if choice == "1":
               self.addbook()
           elif choice == "2":
               self.viewbook()
           elif choice == "3":
               self.searchbook()
           elif choice == "4":
               self.removebook()
           elif choice == "5":
               self.exitlibrary()
           else:
               print("Invalid choice, please try again.")


lib = library()
lib.run()

           









             


              
        
