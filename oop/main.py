'''from library_system import Book, EBook, PrintBook, Library

def main():
    # Part 1: Demonstrating Book magic methods (__str__, __repr__, __del__)
    print("=== Book Magic Methods Demo ===")
    my_book = Book("1984", "George Orwell")
    
    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__
    
    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__
    
    # Deleting a book instance to trigger __del__
    del my_book

    # Part 2: Library System Demo
    print("\n=== Library System Demo ===")
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

    # main.py
# This code demonstrates polymorphism using a Shape class and its subclasses Rectangle and Circle.
# It includes a main function that creates instances of Rectangle and Circle,
# and prints their areas using the area method defined in each subclass.    
;'''
from oop.polymorphism_demo import Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

# main.py

from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")




if __name__ == "__main__":
    main()
# This code demonstrates the use of magic methods in a Book class and a simple library system.
# It includes a main function that creates instances of Book, EBook, and PrintBook,
# adds them to a Library, and lists the books with their details.