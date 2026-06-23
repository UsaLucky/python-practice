#Title: Code to find the roots of quadratic formula
# To allow the user to input the values os a, b and c
a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))

# To find the discriminant
discr =(b**2)-(4*a*c)

# To find the square root of the discriminant
discrsqr =discr**0.5

# To find the value of the numerator if the sign is + or -
num1 = -b + discrsqr
num2 = -b - discrsqr

# To find the value of the demoninator
dem = 2*a

# The value of x when the sign is + or -
x1 = num1 / dem
x2 = num2 / dem

# To output values
print(f"Therefore, your answers will be {x1} and {x2}")