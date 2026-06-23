#Quadratic Formula Solver by Lucky Usa


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

discr = b**2-4*a*c
x1 = (-b + discr**0.5) / (2*a)
x2 = (-b - discr**0.5) / (2*a)

print(f"Therefore, your answers will be {x1} and {x2}")