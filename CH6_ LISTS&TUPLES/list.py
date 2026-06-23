users = ["usa","john" ,"sara"]

data = ["usa", 90, True]

empty = []
 
print("usa" in empty)
print("usa" in users)
print("usa" in data)

print(users[0])
print(users[-1])
#to find the index position for a specific value
print(users.index('sara'))
#to print a range of values i a list
print(users[0:2])
print(users[0:])
#to finf the number of value in a list
print(len(data))
#to add values to a list we use 
#1
users.append("elsa")
print(users)
#2
users+= ['jason', 'mark', 'peter']
print(users)
#3
users.extend(['jim'])
print(users)
#TO ADD a list to another we user
# users.extend(data)
# print(users)
# to insert a value to a specific position we use
users.insert(0, 'Lucky')
print(users)
# to add two or more values in a list we use 
users[2:2] =['Eddie', 'Alex']
print(users)
# to replace values in a list we use 
users[2:6] =['Eddie', 'Alex']
print(users)
# to remove a specific term in a list we use
users.remove('Alex')
print(users)

#to remove thelast value in the list we use the method pop
print(users.pop())
print(users)
#or
users.pop()
print(users) 


#to remove a specific term in a list we can use the keyword del
del users[4]
print(users)

#to delete a list, we can use the keyword del
# del data

# to clear i list we use the method clear
data.clear()
print(data)

#to sort your list maybe alphabetic we use the method sort
users.sort()
print(users)
#Note in this method values in upper case comes before those in lower case
#to fix tis error we can use the key=str.lower
users.sort(key=str.lower)
print(users)

#note this sorting method only works when all the value are of a specfic data type

num = [3.45,43,4,5,23]

#to print something the reverse order of how it was inputed we use
num.reverse()
print(num)
#to sort a list in the reverse order we use the sort method with the parameter reverse
num.sort(reverse=True)
print(num)

#note when you use the sort method you alter the variable . 
#in ordef to print out the sorted version eith out alter the varible we ue

print(sorted(num ,reverse=True))

#to make a copy of a list . there are three ways
#1
numcopy = num.copy()
mynum = list(num)
mycopy = num[:]

print(numcopy)
print(mynum)
print(mycopy)

#you can check the type of list by
print(type(num))

#you can also make a  list using the list constructor
mylist = list([1, 'Niel', True])

