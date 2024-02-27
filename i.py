class Searchable:
    def search_by_title(self, title):
        raise NotImplementedError

    def search_by_author(self, author):
        raise NotImplementedError

    def search_by_genre(self, genre):
        raise NotImplementedError


class Borrowable:
    def borrow_book(self, book):
        raise NotImplementedError

    def return_book(self, book):
        raise NotImplementedError

    def generate_borrowing_report(self):
        raise NotImplementedError


class CatalogManagement:
    def add_book_to_catalog(self, book):
        raise NotImplementedError

    def remove_book_from_catalog(self, book):
        raise NotImplementedError

    def generate_overdue_report(self):
        raise NotImplementedError

    def generate_popularity_report(self):
        raise NotImplementedError


class Librarian(Searchable, Borrowable, CatalogManagement):
    def add_book_to_catalog(self, book):
        print(f"Adding book '{book}' to catalog.")

    def remove_book_from_catalog(self, book):
        print(f"Removing book '{book}' from catalog.")

    def generate_overdue_report(self):
        print("Generating overdue report for books.")

    def generate_popularity_report(self):
        print("Generating book popularity report.")

    def generate_borrowing_report(self):
        print("Generating borrowing report.")

    def borrow_book(self, book):
        print(f"Borrowing the book '{book}'.")

    def return_book(self, book):
        print(f"Returning the book '{book}'.")

    def search_by_title(self, title):
        print(f"Searched for '{title}'.")

    def search_by_author(self, author):
        print(f"Searched for '{author}'.")

    def search_by_genre(self, genre):
        print(f"Searched for '{genre}'.")


class User(Searchable, Borrowable):
    def borrow_book(self, book):
        print(f"Borrowing the book '{book}'.")

    def return_book(self, book):
        print(f"Returning the book '{book}'.")

    def generate_borrowing_report(self):
        print("Generating borrowing report.")

    def search_by_title(self, title):
        print(f"Searched for '{title}'.")

    def search_by_author(self, author):
        print(f"Searched for '{author}'.")

    def search_by_genre(self, genre):
        print(f"Searched for '{genre}'.")


class Guest(Searchable):
    def search_by_title(self, title):
        print(f"Searched for '{title}'.")

    def search_by_author(self, author):
        print(f"Searched for '{author}'.")

    def search_by_genre(self, genre):
        print(f"Searched for '{genre}'.")


def main():
    librarian = Librarian()
    user = User()
    guest = Guest()

    print("\nLibrarian Actions:")
    librarian.add_book_to_catalog("book1")
    librarian.remove_book_from_catalog("book0")
    librarian.generate_overdue_report()
    librarian.borrow_book("book3")
    librarian.return_book("book2")

    print("\nUser Actions:")   
    user.search_by_author("author1")
    user.borrow_book("book1")
    user.return_book("book4")
    user.generate_borrowing_report()

    print("\nGuest Actions:")
    guest.search_by_genre("genre1")


if __name__ == "__main__":
    main()
