def my_func(x, y, z):
    total=x+y+z
    avg=total/3
    sqr=(x*x+y*y+z*z)**0.5
    print(f"Sum: {total:.2f}")
    print(f"Average: {avg:.2f}")
    print(f"Square root of sum of squares: {sqr:.2f}")

x = float(input())
y = float(input())
z = float(input())

my_func(x, y, z)
