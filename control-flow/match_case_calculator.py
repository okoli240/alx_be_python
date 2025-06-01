num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
match (num1, num2, operator):
   case (a, b, "+"):
      print(f"The result is {a + b}.") 
   case (a, b, "-"):
      print(f"The result is {a - b}.") 
   case (a, b, "*"):
      print(f"The result is {a * b}.") 
   case (a, b, "/"):
      if b == 0:
        print("Cannot divide by zero.")
      else:
         print(f"The result is {a / b}.")
      
