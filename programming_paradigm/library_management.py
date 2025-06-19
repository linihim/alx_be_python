class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self._is_checked_out = False
	def check_out(self):
		if not self._is_checked_out:
			self._is_checked_out = True
			return True
		return False
	def return_book(self):
		if self._is_checked_out:
			self._is_checked_out = False
			return True
		return False
	def is_available(self):
		return not self._is_checked_out
	def __str__(self):
		return f"{self.title} by {self.author}"
class Library:
	def __init__(self):
		self._books = []
	def add_book(self, book):
		if isinstance(book, Book):
			self._books.append(book)
		else:
			print("Error: Only Book objects can be added to the library.")
	def _find_book(self, title):
		for book in self._books:
			if book.title == title:
				return book
		return None
	def check_out_book(self, title):
		book_found = self._find_book(title)
		if book_found:
			if book_found.check_out():
				 print(f"'{title}' has been checked out.")
			else:
				print(f"'{title}' is already checked out.")
		else:
			print(f"'{title}' not found in the library.")
	def return_book(self, title):
		book_found = self._find_book(title)
		if book_found:
			if book_found.return_book():
				print(f"'{title}' has been returned.")
			else:
				print(f"'{title}' was not checked out.")
		else:
			print(f"'{title}' not found in the library.")
	def list_available_books(self):
		available_count = 0
		for book in self._books:
			if book.is_available():
				print(book)
				available_count += 1
		if available_count == 0:
			 print("No books are currently available.")



