def perform_operation(num1, num2, operation):
  match operation:
    case "add": return(num1 + num2)
    case "subtract": return(num1 - num2)
    case "mulitply": return(num1 * num2)
    case "divide": 
      if num2 != 0:
        return(num1 / num2)
      else:return("Zero division error")
    
