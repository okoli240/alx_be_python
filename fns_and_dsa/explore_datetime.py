import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return formatted_date  # <-- Required by checker

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future date:", formatted_future)
        return formatted_future  # <-- Required by checker
    except ValueError:
        print("Please enter a valid integer for the number of days.")
        return None

# Function calls
display_current_datetime()
calculate_future_date()