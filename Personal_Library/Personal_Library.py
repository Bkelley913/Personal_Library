# Define the information about the books as tuples
hamlet_info = ("William Shakespeare", "Tragedy", 1603)
martian_chronicles_info = ("Ray Bradbury", "Science fiction", 1950)

# Create a dictionary to store the books with their information
my_books = {"Hamlet": hamlet_info, 
"The Martian Chronicles": martian_chronicles_info}

# Print the dictionary of books
print(f"My books: {my_books}")

# Add a new book to the dictionary with its information
book_info = my_books["Fahrenheit 451"] = ("Ray Bradbury", "Dystopian", 1953)

# Print the information of the new book
print(f"Fahrenheit 451 info: {book_info}")

# Create an empty set to store the authors of the books
my_books_authors = set()

# Iterate through the books in the dictionary
for book in my_books:
  # Get the information of each book  
  book_info = my_books[book]
  # Extract the author from the book information
  author = book_info[0]
  # Add the author to the set of book authors
  my_books_authors.add(author)

# Print the set of authors
print(f'Authors: {my_books_authors}')

# Check if "Ray Bradbury" is in the set of book authors
is_my_author = "Ray Bradbury" in my_books_authors

# Print a message if "Ray Bradbury" is in the set of book authors
if is_my_author:
  print("Ray Bradbury belongs to my authors!")
