import math

try:
    a, b, c = map(float, input().split())

    if a == 0:
        print("No root")  
    else:
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            print("x1 = {:.1f}, x2 = {:.1f}".format(root1, root2))
        elif discriminant == 0:
            root = -b / (2*a)
            print("x = {:.1f}".format(root))
        else:
            print("Imaginary root")
except ValueError:
    print("Wrong input")

print("Done")
