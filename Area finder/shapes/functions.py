import math

#   -----------FUNCTIONS----------  #

#  ---- Circle ----  #
def circle():
    Radius = float(input("Enter the radius of circle: "))
    area = math.pi * (Radius**2)
    
    if Radius<=0:
        print("Radius must be positive number \n")
        return 
    
    area = math.pi * (Radius**2)
    print(f"The area of circle is {area}")

#  ---- Square ----  #
def square():
    lenght = float(input("Enter the lenght of one side of square: "))
    
    if lenght <= 0 :
        print("Lenght must be positive number \n")
        return
    
    area = lenght**2
    print(f"The area of square is {area}")

#  ---- Triangle ----  #
def triangle():
    base = float(input("Enter the base of one side of triangle: "))
    height = float(input("Enter the height of one side of triangle: "))
    
    if base <= 0 or height <= 0:
        print("Base and Height must be positive number \n")
        return
    
    area = 0.5 * base * height
    print(f"The area of triangle is {area}")

#  ----- Rectangle ----  #
def rectangle():
    lenght = float(input("Enter the lenght of one side of rectangle: "))
    width = float(input("Enter the width of one side of rectangle: "))
    
    if lenght <= 0 or width <= 0:
        print("Lenght and width must be positive number \n")
        return 
    
    area = lenght * width
    print(f"The area of Rectangle is {area}")


#  ----- Parallellogram ----  #
def parallelogram():
    base = float(input("Enter the base of one side of Parallelogram: "))
    height = float(input("Enter the height of one side of Parallelogram: "))
    
    if base <= 0 or height <= 0:
        print("Base must be positive number \n")
        return
    
    area = base * height
    print(f"The area of Parallelogram is {area}")    


#  ---- Trapezium ----  #
def trapezium():
    base1 = float(input("Enter the first base of one side of Trapezium: "))
    base2 = float(input("Enter the second base of one side of Trapezium: "))
    height = float(input("Enter the height of one side of Trapezium: "))
    
    if base1 <= 0 or base2 <= 0 or height <= 0:
        print("Base and Height must be positive number \n")
        return
    
    area = 0.5 * (base1 + base2) * height
    print(f"The area of Trapezium is {area}")

#  ---- Rombus ----  #
def rhombus():
    diagonal1 = float(input("Enter diagonal 1: "))
    diagonal2 = float(input("Enter diagonal 2: "))
    
    if diagonal1 <= 0 or diagonal2 <= 0:
        print("Diagonals must be positive number \n")
        return
    
    area = 0.5 * diagonal1 * diagonal2
    print(f"The area of Rombus is {area}")

#  ---- Ellipse ----  #
def ellipse():
    axis_a = float(input("Enter semi-major axis (a): "))
    axis_b = float(input("Enter semi-minor axis (b): "))
    
    if axis_a <= 0 or axis_b <= 0:
        print("Values must be positive\n")
        return
    
    area = math.pi * axis_a * axis_b
    print(f"The area of Ellipse is {area}")