import math

def calculate_square():
    side =float(input("Enter the side of Square"))
    area = side**2
    perimeter = 4*side
    print("Area of Square =",area)
    print("parimeter of square =",perimeter)

def calculate_rectangle():
    length=float(input("enter the length of the rectangle:"))
    width = float(input("Enter the width of the rectangel"))

    area = length*width
    perimeter = 2*(length+width)
    print("Area of rectangle =",area)
    print("perimeter of rectange =",perimeter)
def calculate_circle():
    radius = float(input("Enter the radius of the circle :"))
    area = math.pi * radius**2
    perimeter = 2*math.pi*radius
    print("Area or circle =%.2f"%area)
    print("perimeter of circle=%.2f"%perimeter)

def calculate_triangle():
    base = float(input("Enter side Base of th triangle "))
    height=float(input("Enter the height of the triangle"))
    a = float(input("Enter side a of th triangle "))
    b = float(input("Enter side b of th triangle "))
    c = float(input("Enter side c of th triangle "))

    area = 1/2*base*height

def main():
 while True:
    print("Welocme to the Area & perimeter Calculator!")
    print("Choose a shape:")
    print("1.Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")

    choice =input("Enter your choice(1-4):)")

    if choice == '1':
        calculate_square()
    elif choice=='2':
        calculate_rectangle()
    elif choice == '3':
        calculate_circle()
    elif choice =='4':
        calculate_triangle()
    else:
        print("invalid choice ! Please run the program again.")

    again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
    if again != 'yes':
            print("Thank you for using the calculator!")
            break

main()