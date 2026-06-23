#tuple

mytuple = tuple([1, 'Niel', True])
anothertuple =(1,2,3,6,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

#since tuple can not be change or rearranged we can make a copy of a tuple as a list
newlist = list(mytuple)
newlist.append('niel')


newtuple = tuple(newlist)
print(newtuple)
 

#assign values to a tuple is cslled packing. note we can also unpack a tuple

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

(*one, two, hey) = anothertuple
print(one)
print(two)
print(hey)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

#to count how many times a value appears in a tuple we useth count method
print(anothertuple.count(2))