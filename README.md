# Personal_Library

This code represents a personal library where you can store information about books. It utilizes dictionaries, tuples, and sets to organize and retrieve book data. Below is an overview of the code and its functionality.

## Code Overview

### Book Information

The code starts by defining information about books using tuples. Each tuple represents the information about a book, including the author, genre, and publication year.

### Creating the Library

A dictionary named `my_books` is created to store the books as key-value pairs. The book titles serve as the keys, while the corresponding book information tuples are the values.

### Printing the Library

The code prints the dictionary `my_books` to display the collection of books along with their information.

### Adding a New Book

A new book, "Fahrenheit 451," is added to the library by assigning its information tuple to the dictionary using the key "Fahrenheit 451". The code then prints the information of the newly added book.

### Extracting Authors

An empty set `my_books_authors` is created to store the unique authors of the books. The code iterates through the books in the `my_books` dictionary. For each book, it extracts the author from the book information tuple and adds it to the set of authors.

### Printing Authors

The set of authors `my_books_authors` is printed to display the unique authors in the personal library.

### Checking for an Author

The code checks if the author "Ray Bradbury" is present in the set of book authors `my_books_authors`. It assigns the result to the variable `is_my_author`.

### Printing Author Membership

If "Ray Bradbury" is found in the set of book authors, the code prints a message indicating that "Ray Bradbury" belongs to the set of authors.

## Usage

To use this code, simply run the script. It will display the output for the library contents, book information, authors, and author membership.

Feel free to modify the book information, add more books, or customize the code to suit your personal library needs.
