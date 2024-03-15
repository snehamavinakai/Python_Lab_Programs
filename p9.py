def calculate_rectangle_area(length,width):
    area = length * width
    return area

def calculate_circle_area(radius):
    import math
    area = math.pi*radius**2
    return area

def greet(name):
    print(f'HELLO {name}!')

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "odd"
    
if __name__ == '__main__':
    length = 5
    width = 3
    rectangle_area = calculate_rectangle_area(length,width)
    print("Area of Rectangle : ",rectangle_area)
    
    radius = 4
    circle_area = calculate_circle_area(radius)
    print("Area of Circle : ",circle_area)

    name = "Sneha"
    greet(name)
    
    number = 3
    result = is_even_or_odd(number)
    print(number,"is = ",result)
    