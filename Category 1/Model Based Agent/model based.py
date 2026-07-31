# ============================================
# Model Based Agent
# Smart Library
# ============================================

class Library:

    def __init__(self):
        self.books = {
            "Python": 5,
            "AI": 4,
            "Java": 3
        }

    def display(self):
        print("\nCurrent Books")
        print("-" * 25)

        for book in self.books:
            print(book, ":", self.books[book])

    def borrow(self, book):

        if book not in self.books:
            print("Book Not Found")
            return

        if self.books[book] > 0:
            self.books[book] -= 1
            print(book, "Borrowed Successfully")

            if self.books[book] <= 1:
                print("Warning:", book, "stock is low")

        else:
            print("Book Not Available")


library = Library()

while True:

    library.display()

    book = input("\nEnter book name: ")

    library.borrow(book)

    again = input("\nBorrow another? (yes/no): ")

    if again.lower() == "no":
        break