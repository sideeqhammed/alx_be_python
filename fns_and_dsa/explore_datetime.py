from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now()
  current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {current_date}")

display_current_datetime()

def calculate_future_date():
  future_date = int(input("Enter a number of days: "))
  duration = timedelta(days = future_date)
  new_date = datetime.today().date() + duration
  print(f"Future date: {new_date}")

calculate_future_date()