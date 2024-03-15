def create_tuple():
    my_tuple = ()
    print("Empty tuple is created")
    return my_tuple

def add_to_tuple(my_tuple,element):
    my_tuple += (element,)
    print(f'Added {element} to the tuple')
    return my_tuple

def access_tuple(my_tuple,index):
    if 0<= index < len(my_tuple):
        element = my_tuple[index]
        print(f'Element at index {index} : {element}')
    else:
        print("Invalid index")
        
def remove_from_tuple(my_tuple,element):
    if element in my_tuple:
        my_list = list(my_tuple)
        my_list.remove(element)
        my_tuple = tuple(my_list)
        print(f'Removed {element} from tuple.')
        return my_tuple
    else:
        print(f'{element} not found in tuple')

def display_tuple(my_tuple):
    print("Cuurent  tuple : ",my_tuple)
my_tuple = create_tuple()
 

while True:
    
    print("\nChoose an action : ")
    print("1.Add an element to tuple : " )
    print("2.Access an element in the tuple : ")
    print("3.Remove an element from the tuple : ")
    print("4.Display the current tuple")
    print("5.Exit")

    choice = input("Enter you choice (1/2/3/4/5) : ")
    
    if choice == '1':
        element = input("Enter an elements to add : ")
        my_tuple=add_to_tuple(my_tuple,element)
    elif choice == '2':
        index = int(input("Enter the index to access : "))
        access_tuple(my_tuple,index)
    elif choice == '3':
        element = input("Enter an element to remove : ")
        my_tuple = remove_from_tuple(my_tuple,element)
    elif choice  == '4':
        display_tuple(my_tuple)
    elif choice == '5':
        break
    else:
        print("Invalid choice,please try again...")
        