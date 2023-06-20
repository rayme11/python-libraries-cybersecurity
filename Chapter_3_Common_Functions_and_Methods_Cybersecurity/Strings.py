str = ' Python '

# colons sets up a range
str = str[1:7]
print(str)

# start at position 2 until end of string
str = str[2:]
print(str)

# checking for string inside another string

str = "Raymundo"

print('Mundo' in str)  # false
print('mundo' in str)  # true

# printing chars multiple times
print('*'*20)

# formatting
print('Hi {}. {} Day!'.format("Ray", "Good"))

# specifying positional arguments
print('Hi {1}. {0} Day!'.format("Good", "Ray"))

# rindex - get index from string within a string
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

# Join all items in a tuple into a string, using a hash character as separator:

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# Join all items in a dictionary into a string, using the word "TEST" as separator:
# Note: When using a dictionary as an iterable, the returned values are the keys, not the values.
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

# Split a string into a list where each word is a list item:

txt = "welcome to the jungle"
x = txt.split()
print(x)
print(len(x))
print(x[0])

# Return the number of times the value "cherry" appears in the fruits list:

fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
