import math as MA
n = eval(input())
s = eval(input())

area = (n * (s**2))/(4*MA.tan(MA.pi/n))
print(f"Area = {area:.4f}")