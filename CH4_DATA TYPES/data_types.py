import math 

#string data type
# literal assignment
first = "Usa"
last = "John"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#concatanation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "i like music from the " + decade + "s."
print(statement)

# multiply lines
multiline = '''Hey, how are you? 

I was just checking in.
                            All good?
'''
print(multiline)

# Escaping special character
sentence= 'I\'m back at work\t hey\n\nWhere\'s this at \\located'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline+= "                        "
multiline = "               " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip())) 
print(multiline.strip())
# for practice
# var2 = "    hi   "
# print(len(var2))
# print(len(var2.strip()))
# print(len(var2.rstrip()))
# print(len(var2.lstrip()))

print("  ")

#build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffe".ljust(16, ".")+ "$1".rjust(4))
print("Muffin".ljust(16, ".")+ "$2".rjust(4))
print("Cheesecake".ljust(16, ".")+ "$3".rjust(4))

print("  ")
# for practice
# title2 = "TOC".upper()
# print(title2.center(40, "="))
# print("Group Members".ljust(35, ".")+"i".rjust(5))
# print("Abstract".ljust(35, ".")+"ii".rjust(5))
# print("Table of COntent".ljust(35, ".")+"iii".rjust(5))

#String index values
print(first[1])
print(first[-1])
print(first[1:-1])

#some methods return boolean dat
print(first.startswith("U"))
print(first.endswith("U"))

print("  ")

#boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#numeric Data 
#integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(myvalue, int))

#float type
gpa = 4.57656443
y = float(1.11)
print(type(gpa))

#complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag )

# to add to complex number(practice)
# num1 = 4+9j
# num2 = 4- 2j
# add = num1+num2
# print(add)

#built in function for number
print(abs(gpa))
#Note abs() round the number to it 2 decimal point

print(round(gpa))
print(round(gpa, 1))
print(round(gpa, 3))
# The method round is used to round a float to a specific degree


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
# The method ceil round up a number to the upper whole number
print(math.floor(gpa))
# The method floor round up a number to the lower whole number

# Casting a string to a number
zipcode ="10001"
zip_value = int(zipcode)
print(type(zip_value))

# You can get an error if you attempt to cast incorrect data
# zip_value= int("New york") 

