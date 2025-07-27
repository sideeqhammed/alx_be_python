FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f"{fahrenheit}°F is {celcius}°C")


def convert_to_fahrenheit(celsius): 
  farenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
  print(f"{celsius}°C is {farenheit}°F")

temp = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

match unit:
  case "C": convert_to_fahrenheit(temp)
  case "F": convert_to_celsius(temp)
  case _: print("Invalid temperature. Please enter a numeric value.")