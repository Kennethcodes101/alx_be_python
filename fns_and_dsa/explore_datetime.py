import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date)

def calculate_future_date():
    
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    print(f"Future Date:", future_date)


display_current_datetime()
calculate_future_date()