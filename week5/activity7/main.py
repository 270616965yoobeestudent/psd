# LibraryItem is base class for Book and Magazines
# all attributes are protected because they're allowed to access by subclass 
class LibraryItem:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    # information LibraryItem
    def info(self):
        return f"{self._title} by {self._author}"

    # create getter method for protected attribute because it needs for filtered items
    def title(self):
        return self._title


# Book is subclass of LibraryItem
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title, author)

    # Override info method from LibraryItem
    def info(self):
        return f"Book {self._title} by {self._author}"

# Magazines is subclass of LibraryItem
class Magazines(Book):
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self._issue_frequency = issue_frequency

    # Override info method from LibraryItem
    def info(self):
        return f"Magazines {self._title} by {self._author} {self._issue_frequency}"


# Library is a class that contain LibraryItem in a list
class Library:
    def __init__(self, items):
        self._items = items

    # Add more LibraryItem which is including its subclass Book and Magazines
    # This is polymorphism
    def add(self, item):
        self._items.append(item)

    # Remove item by title
    # title can't access directly because it's protected.
    # title() is getter from LibraryItem
    def remove(self, title):
        self._items = [item for item in self._items if item.title() != title]

    # Show all LibraryItem which will use info() that override from subclass
    def show_items(self):
        for item in self._items:
            print(item.info())


def main():
    book1 = Book("The Alchemist", "Paulo Coelho")
    book2 = Book("The Da Vinci Code", "Dan Brown")
    magazines1 = Magazines("The Times", "John Doe", "Monthly")

    library = Library([])
    library.add(book1)
    library.add(book2)
    library.add(magazines1)
    library.show_items()

    library.remove("The Da Vinci Code")
    library.show_items()


if __name__ == "__main__":
    main()
