class User(object):
	def __init__(self, name, email):
		assert("@" in email and (".com" or ".org" or ".edu")), "This is an invalid email address format."
		self.name = name
		self.email = email
		self.books = {}

	def get_email(self):
		return self.email

	def change_email(self, address):
		self.email = address
		return self.email
		print("You've successfully changed your email address to " + address + ".")

	def __repr__(self):
		return "User {}, email: {}, books read: {}".format(
			self.name, self.email, len(self.books)
			)
		print(user_summary)

	def __eq__(self, other_user):
		return self.name == other_user.name and self.email == other_user.email

	def read_book(self, book, rating=None):
		self.books[book] = rating

	def get_average_rating(self):
		sum_ratings = 0
		avg_ratings = 0
		for rating in self.books.values():
			if rating is not None:
				sum_ratings += rating
		avg_ratings = sum_ratings / len(self.books.values())
		return avg_ratings

class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []

	def get_title(self):
		return self.title

	def get_isbn(self):
		return self.isbn

	def set_isbn(self, isbn_new):
		self.isbn = isbn_new
		return "This book's ISBN has been updated for {} to {}".format(
			self.title, isbn_new
			)

	def add_rating(self, rating):
		if rating >= 0 and rating <= 4:
			self.ratings.append(rating)
		else:
			print("Invalid rating")

	def __eq__(self, other_book):
		return self.title == other_book.title and self.isbn == other_book.isbn

	def get_average_rating(self):
		sum_ratings = 0
		for rating in self.ratings:
			sum_ratings += rating
		return sum_ratings / len(self.ratings)

	def __hash__(self):
		return hash((self.title, self.isbn))

class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author

	def get_author(self):
		return self.author

	def __repr__(self):
		return "{} by {}".format(
			self.title, self.author
			)

class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level

	def get_subject(self):
		return self.subject

	def get_level(self):
		return self.level

	def __repr__(self):
		return "{}, a {} manual on {}.".format(
			self.title, self.level, self.subject
			)

class TomeRater(object):
	def __init__(self):
		self.users = {}
		self.books = {}

	def create_book(self, title, isbn):
		return Book(title, isbn)

	def create_novel(self, title, author, isbn):
		return Fiction(title, author, isbn)

	def create_non_fiction(self, title, subject, level, isbn):
		return Non_Fiction(title, subject, level, isbn)

	def add_user(self, name, email, user_books=None):
		if email in self.users:
			print("A user with email address {} already exists".format(email))
		else:
			self.users[email] = User(name, email)
			if user_books is not None:
				for book in user_books:
					self.add_book_to_user(book, email)

	def add_book_to_user(self, book, email, rating=None):
		if email not in self.users:
			print("No user with e-mail {}!".format(email))
		else:
			self.users[email].read_book(book, rating)
			if rating != None:
				book.add_rating(rating)
			if book in self.books:
				self.books[book] += 1
			else:
				self.books[book] = 1

	def print_catalog(self):
		for book  in self.books:
			print(book)

	def print_users(self):
		for user in self.users:
			print(user)

	def most_read_book(self):
		return max(self.books, key=self.books.get)

	def highest_rated_book(self):
		highest_rate = 0
		rated_book = None
		for book in self.books:
			score = book.get_average_rating()
			if score > highest_rate:
				highest_rate = score
				rated_book = book
		return rated_book

	def most_positive_user(self):
		highest_avg = 0
		highest_avg_user = None
		for user in self.users.values():
			score = user.get_average_rating()
			if score > highest_avg:
				highest_avg = score
				highest_avg_user = user
		return highest_avg_user