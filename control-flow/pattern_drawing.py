# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while
while row < size:
    # Inner loop using for
    for column in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row
    row += 1