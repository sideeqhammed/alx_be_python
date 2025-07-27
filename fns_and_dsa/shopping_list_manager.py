
def display_menu():
  print("Shopping List Manager")
  print("1. Add Item")
  print("2. Remove Item")
  print("3. View List")
  print("4. Exit")

  

def main():
  shopping_list = []
  checker = True
  while checker:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
      new_item = input("Enter a new item to add: ")
      shopping_list.append(new_item)
      print()

    elif choice == 2:
      remove_item = input("Enter an item to remove: ")
      if remove_item in shopping_list:
        shopping_list.remove(remove_item)
      else: print("Item doesn't exist")
      print()

    elif choice == 3: 
      print("Here is your shopping list:")
      print(shopping_list)
      print()

    elif choice == 4: 
      print("Goodbye!")
      checker = False

    else: print("Invalid choice. Please try again.")
    print()

if __name__ == "__main__":
  main()
