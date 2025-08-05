def safe_divide(numerator, denominator):
  try: 
    numerator = float(numerator)
    denominator = float(denominator)

    reult = numerator / denominator

  except ZeroDivisionError as e:
    return("Error: Cannot divide by zero.")
  
  except ValueError as e:
    return("Error: Please enter numeric values only.")

  else: return numerator / denominator