from library_management import Book, Library
def main():
	library = Library()
	library.add_book(Book("Brave New World", "Aldous Huxley"))
	library.add_book(Book("1984", "George Orwell"))
	
	print("Available books after setup:")
	library.list_available_books()

	library.check_out_book("1984")
	print("\nAvailable books after checking out '1984':")
	library.list_available_books()

	library.return_book("1984")
	print("\nAvailable books after returning '1984':")
	library.list_available_books()

	print("\n--- Additional Tests ---")
	library.check_out_book("Nonexistent Book") 
	library.check_out_book("Brave New World") 
	library.check_out_book("Brave New World") 
	print("\nAvailable books after more operations:")
	library.list_available_books()
	library.return_book("Nonexistent Book") 
	library.return_book("Brave New World") 
	library.return_book("Brave New World") 
	print("\nAvailable books after final operations:")
	library.list_available_books()

if __name__ == "__main__":
	main()
