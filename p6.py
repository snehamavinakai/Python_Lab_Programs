def create_list():
    global my_list
    my_list = []
    print("New empty list created.")
    #return my_list

def append_to_list(element):
    my_list.append(element)
    print(f'Appended {element} to the list.')

def remove_from_list(element):
  try:
    my_list.remove(element)
    print(f'Removed {element} from the list')
  except ValueError:
    print(f'{element} not found in list')

def display_list():
    print("Current List",my_list)

while True:
    print("\nChoose an action")
    print("1.Create a new list")
    print("2.Append an element to the list")
    print("3.Remove an element from the list")
    print("4.Display the current list")
    print("5.Exit")
    
    choice = input("Enter your choice(1/2/3/4/5) :")
    
    if choice == '1':
        create_list()
    elif choice =='2':
        element = input("Eneter an element to append : ")
        append_to_list(element)
    elif choice == '3':
        element = input("Enter an element to remove :")
        remove_from_list(element)
    elif choice == '4':
        display_list()
    elif choice == '5':
        break 
    else:
        print("Invalid choice. Please try again")