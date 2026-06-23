# a= 5
# b = 6
# c = 7

# print(a + b+ c)
# print(a - b- c)
# print(a * b* c)
# print(a / b/ c)

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))
oper =str(input("Choose between  +, -, *, /"))
if oper == "+" :
    result = a+b+c
elif oper == "-":
    result = a-b-c
elif oper == "*":
    result = a*b*c
elif oper == "/":
    result = a/b/c
else:
    print('Please input +, -, /, *')
print(f"Your answer is {result}")