def printSolutionQuadratic(a, b, c):
    if a == 0 and b != 0:  # Linear equation: bx + c = 0
        x = -c / b
        print(f"There is one root and it is {x}")

    elif a == 0 and b == 0:  # Equation: c = 0
        print("There is no x to solve for! No roots!")

    elif a != 0 and b**2 - 4*a*c == 0:
        x = (-b) / (2*a)
        print(f"There is one root and it is {x}")

    elif a != 0 and b**2 - 4*a*c < 0:
        print("There are no real roots!")

    elif a != 0 and b**2 - 4*a*c > 0:
        delta = b**2 - 4*a*c
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print(f"There are two roots and they are {x1} and {x2}")

    else:
        print("Oh something went wrong, I didn't expect to get here")


# Inputs
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

printSolutionQuadratic(a, b, c)