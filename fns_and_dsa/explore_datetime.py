from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now()
  current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {current_date}")

display_current_datetime()

def calculate_future_date():
  number_of_days = int(input("Enter the number of days to add to the current date: "))
  duration = timedelta(days = number_of_days)
  future_date = datetime.today().now() + duration
  future_date = future_date.strftime("%Y-%m-%d")
  print(f"Future date: {future_date}")

calculate_future_date()