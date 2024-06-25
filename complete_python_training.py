# print("Hello, world!")
# variables
# creating variables
# x =5
# y ="Patience"
# print(x)

#Example 1
# x = 5
# y = "john"
# print(type(x))
# print(type(y))

#Example 2 
# a = 4
# A = "Sally"
# print(a)
# print(A)

#Many values to multiple variable
x,y,z = 'orange', 'banana', 'cherry'
print(x)
print(y)
print(z)

#one values to multiple variable
x=y=z ='orange'
print(x)
print(y)
print(z)

#unpack a list
fruits =['apple','banana', 'cherry']
x,y,z = fruits
print(x)
print(y)
print(z)

#output variable (print() functions)
x= "Python is awesome"
print(x)

x= 'Python'
y= 'is'
z= 'awesome'
print(x,y,z) 

# + operator
x=5
y=10
print(x + y)

x=5
y='Patience'
print(x,y)

# global variables
# create a variable of a function, and use it inside the function
x = 'awesome'
def myfunc():
    print("Python is " + x)
myfunc()

# create a variable inside a function, with the same name as the global variable and use it inside the function
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()    

# global keyword
def myfunc():
    global x
    x = 'fantastic'
myfunc()
print('Python is ' + x)    
     
#global keyword
x = 'awesome'
def myfunc():
    global x
    x = 'fantastic'
myfunc()
print('Python is ' + x) 

#Exercise 1: create a variable named carname and assign the value volvo to it.
carname = "volvo"

#Exercise 2: create a variable named x and assign the value 50 to it
x = 50

#Exercise 3: Display the sum of 5 + 10, using two variables: x and y
x = 5
y = 10
print(x+y)

#Exercise 4: create a variable called z, assign  x + y to it, and display the result
x = 5
y = 10
z = x + y
print(z)

#Execise 5: insert the correct syntax to assign values to multiple variables in one line:
x,y,z = 'apple','banana', 'cherry'
print(x,y,z)
    
# Insert the correct syntax to assign the same value to all three variables in one code line
x=y=z = 'Banana'
print(z)  

#Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

#The following code example would print the data type of x, what data type would that be?
x = 5
print(type(x))

# Data Variable
#Print the data type of the variable x:
x = 5
print(type(x))

#Exercise 1: The following code example would print the data type of x, what data type would that be?
x = 5
print(type(x))

#Exercise 2: The following code example would print the data type of x, what data type would that be?
x = "Hello World"
print(type(x))

#Excercise 3: The following code example would print the data type of x, what data type would that be?
x = "Hello World"
print(type(x))

#Exercise 4: The following code example would print the data type of x, what data type would that be?
x = 20.5
print(type(x))

#Exercise 5:The following code example would print the data type of x, what data type would that be?
x = 20.5
print(type(x))

#Exercise 6: The following code example would print the data type of x, what data type would that be?
x = ["apple", "banana", "cherry"]
print(type(x))

#Exercise 7: The following code example would print the data type of x, what data type would that be?
x = ("apple", "banana", "cherry")
print(type(x))

#Exercise 8: The following code example would print the data type of x, what data type would that be?
x = {"name" : "John", "age" : 36}
print(type(x))
 
#Exercise 9: The following code example would print the data type of x, what data type would that be?
x = True
print(type(x))

#Exercise 10: Insert the correct syntax to convert x into a floating point number.
x = 5
x = float(x)

#Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#Random numbers
#Import the random module, and display a random number between 1 and 9
import random
print(random.randrange(1, 10))

#strings
print("Hello")

#quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assigning variables
a = "Hello"
print(a)

#multilines strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings are arrays
#Get the character at position 1 (remember that the first character has the position 0)
a = "Hello, World!"
print(a[1])

#loops through a string
#Loop through the letters in the word "banana":
for x in "banana":
    print(x)

#string length
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a)) 

#check strings
#Example 1: Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#Example 2:Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#check if not
#Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)

#print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#slicing strings
#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#Slice From the Start
#By leaving out the start index, the range will start at the first character:
#Example :Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

#Slice To the End
#By leaving out the end index, the range will go to the end:
#Example: Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

#Negative indexing
#Example:Get the characters:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])

# upper case: upper()
a = "Hello, World!"
print(a.upper())

#lower case: lower()
a = "Hello, World!"
print(a.lower())
#whitespace: strip() removes the whitespace in the sentence.
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#replace string: replace method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#split strings: The split() method returns a list where the text between the specified separator becomes the list items.
#Example: 
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation: To concatenate, or combine, two strings you can use the + operator.
#Example: Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

#Example: to add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)
#f- string(formating string)
#Example: Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers:A placeholder can contain variables, operations, functions, and modifiers to format the value.
#Example:Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Example:Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)

#escape character
#Example:The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods return new values. They do not change the original string.
# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

#string Exercise:
#Exercise 1:Use the len function to print the length of the string.
x = "Hello World"
print(len(x))
#Exercise 2:Get the first character of the string txt.
txt = "Hello World"
print(txt[0])
#Exercise 3: Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
print(txt[2:5])
#Exercise 4: Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
print(txt.strip())

#Exercise 5: Convert the value of txt to upper case.
txt = "Hello World"
print(txt.upper())

#Exercise 6:Convert the value of txt to lower case.
txt = "Hello World" 
print(txt.lower())

#Exercise 7:replace the character H with a J.
txt = "Hello World"
print(txt.replace("H","J"))

#Exercise 8: Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#BOOLEAN
# #Example: 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Example 2: Print a message based on whether the condition is True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate values and variables
#Example 1: Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

#Example 2: Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# MOST VALUES ARE TRUE
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

#Example 1: The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Some Values are False
#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

#Example 1:The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Example 2. Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
#Example 1: Check if an object is an integer or not:
x = 200
print(isinstance(x, int))

#PYTHON OPERATOR
#Example 1:
x = 5
y = 3
print(x + y) #Addition

#Example 2:
x = 5
y = 3
print(x - y)

#Example 3:
x = 5
y = 3
print(x * y) #multiplication

#Example 4:
x = 12
y = 3
print(x / y) #Division

#Exercise 1:Multiply 10 with 5, and print the result.
print(10*5)

#Exercise 2: Divide 10 by 2, and print the result.
print(10/2)

#Exercise 3: Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Exercise 4: Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
  print("5 and 10 is not equal") 

#Exercise 2: Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true") 

#LIST
#Example 1: String, int and boolean data types:
List1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False] 

#Example 2: A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#Example 3:What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Example 3: Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access Items:List items are indexed and you can access them by referring to the index number:
#Example 1:Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Example 2:This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#Example 2: This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Example 3:This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Example 4: This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Example 5:Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Example 6: Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Example 7:Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Append Items
#To add an item to the end of the list, use the append() method:
#Example 1:Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items :To insert a list item at a specified index, use the insert() method.The insert() method inserts an item at the specified index:
#Example 1.Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#extend list
#Example 1: Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#ADD ANY ITERABLE
#Example 1:Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#REMOVE LIST ITEMS
#Example 1.Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index:The pop() method removes the specified index.
#Example 1:Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#DEL :The del keyword also removes the specified index:
#Example 1: Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)

#DEL THE ENTIRE LISR: The del keyword can also delete the list completely.
#Example 1: Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

#CLEAR THE LIST: EMPTIES THE LIST
#Example 1:Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Example 2:Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#LOOP THROUGH THE INDEX NUMBER
#Example 1: Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Looping Using List Comprehension: List Comprehension offers the shortest syntax for looping through lists:
#Example 1: A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#LIST COMPREHENSION:
#EXAMPLE 1: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#LIST WITH CONDITIONS :The condition is like a filter that only accepts the items that valuate to True.
#Example:Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#ITERABLE: The iterable can be any iterable object, like a list, tuple, set etc.
#Example 1:You can use the range() function to create an iterable:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in range(10)]
print(newlist)

#Expression
#Example 1:Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#Example 2:Set all values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

#Example 2: Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#Sort List Alphanumerically:List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#Example 1:Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Example 2: Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending:To sort descending, use the keyword argument reverse = True:
#Example 1:Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Example 2:Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Case Insensitive Sort:By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
#Example 1:Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Example 2:Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#REVERSE ORDER
#Example 1:Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#COPY LIST
#Example 1:Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Example 2:Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#JOIN LISTS
#Example 1: Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Example 2: Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#Example 2: Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#Exercise  for python list
#1.Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])


# 2.Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"
print(fruits)

# 3.Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# 4.Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)

# 5.Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

# 6.Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# 7. Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# 8.Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#TUPLES
#Example 1.Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Example 3.Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Example 4:Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Example 1:One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Example 1. A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#Example 2.What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Example 1.Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Example 1. This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Example 2.Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Example 2.Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Example 1:Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Example 2:Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#REMOVING ITEMS
#Example 1.Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) 

#DELETE THE ITEMS
#Example 1.The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Loop Through a Tuple:You can loop through the tuple items by using a for loop.
#Example:Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Example:Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# USING WHILE LOOP
#Example:Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join Two Tuples:To join two or more tuples you can use the + operator:
#Example:Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Join Two Tuples: To join two or more tuples you can use the + operator:
#Example:Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples:If you want to multiply the content of a tuple a given number of times, you can use the * operator:
#Example:Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#Exercise 1: Print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Exercise 2: Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Exercise 3:Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Exercise 4:Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#SET
#Duplicates Not Allowed: Sets cannot have two items with the same value.
#Example 1:Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#Example 1:True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#Example 2:False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#PYTHON SET:Sets are written with curly brackets.
myset = {"apple", "banana", "cherry"}
print(myset)

#Example:False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#Example:Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Get the Length of a Set To determine how many items a set has, use the len() function.
#Example:Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Example:String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1, set2, set3)

#Example:What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Example:Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Example:Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#Add items:To add one item to a set use the add() method.
#Example:Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add Sets:To add items from another set into the current set, use the update() method.
#Example:Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Example:Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove Item:To remove an item in a set, use the remove(), or the discard() method.
#Example:Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Example:Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#Example:The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#Example:The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #thisset is not defined

#loop items: You can loop through the set items by using a  for loop
#Example:Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Example:Get Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Example:Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#Example:Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

#Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
#The result will be a set.
#Example:Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#Example:The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Intersection:Keep ONLY the duplicates.The intersection() method will return a new set, that only contains the items that are present in both sets.
#Example:Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

#Example:Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

#Example:Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#Example:Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#Different
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
#Example:Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)


#Exercise:Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Exercise:Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits) 


#Exercise:Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

#DICTIONARY
#Dictionary:Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Example:Create and print a dictionary:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict)

#Example:Print the "brand" value of the dictionary:
thisdict = {"brand": "Ford", "model": "Mustang","year": 1964}
print(thisdict["brand"])

#Example:Duplicate values will overwrite existing values:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964,"year": 2020}
print(thisdict)

#Example:String, int, boolean, and list data types:
thisdict = {"brand": "Ford","electric": False, "year": 1964,"colors": ["red", "white", "blue"]}
print(thisdict)

#Example:Print the data type of a dictionary:
thisdict = {"brand": "Ford",  "model": "Mustang","year": 1964}
print(type(thisdict))

#The dict() Constructor:It is also possible to use the dict() constructor to make a dictionary.
#Example:Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Example:Get the value of the "model" key:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict["model"])

#get() method
thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
x = thisdict.get("model")
print(x)

#Get Values:The values() method will return a list of all the values in the dictionary.
#Example:Get a list of the values:
thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
x = thisdict.values()
print(x)

#Example:Make a change in the original dictionary, and see that the values list gets updated as well:
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Example:Check if "model" is present in the dictionary:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Values:You can change the value of a specific item by referring to its key name:
#Example:Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#update() method
#Example:Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#Adding Items:Adding an item to the dictionary is done by using a new index key and assigning a value to it:
#Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Example:Add a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Example:The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#Example:The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#Example:The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Example:Print all key names in the dictionary, one by one:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#Example:Print all values in the dictionary, one by one:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
 
#Example:You can also use the values() method to return values of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
  
#Example:You can use the keys() method to return the keys of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

#Example:Loop through both keys and values, by using the items() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

# Example:Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

#Exercise
#1.Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]= 2020
print(car)

#3Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
print(car)

#Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

#Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

# if statement
#Example:If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Elif:The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else:The else keyword catches anything which isn't caught by the preceding conditions.
#Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#If_elif_else
#Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#And:The and keyword is a logical operator, and is used to combine conditional statements:
#Example:Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")  
 
#Or:The or keyword is a logical operator, and is used to combine conditional statements:
#Example:Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Not:The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
#Example:Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Nested If:You can have if statements inside if statements, this is called nested if statements.
#Example
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

  #Exercise
  # 1.Print "Hello World" if a is greater than b.
a = 50
b = 10
if a > b:
  print("Hello World")  

# 2.print "Hello World" if a is not equal to b.
a = 50
b = 10
if a != b:
   print("Hello World")

#Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")  

#Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10  
if a ==b:
  print(1)
elif a > b:
  print(2)
else:
  print(3)    

#Print "Hello" if a is equal to b, and c is equal to d.
a = 50
b = 50
c = 60
d = 60
if a == b and c == d:
  print("Hello")

# Python while loop
#Example:Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1

#The break Statement"With the break statement we can stop the loop even if the while condition is true:
#Example:Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Example:Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) 

#Example:Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Exercise:Print i as long as i is less than 6.
i = 1
while i < 6:
  print(i)
  i += 1

#Exercise:Stop the loop if i is 3.
i = 3
while 1 == 3:
  print(i)
  break
  i += 1

#Exercise:In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
   continue
   print(i)

#Exercise:Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#for loop
#Example:Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Example:Loop through the letters in the word "banana":
for x in "banana":
  print(x)
  
#Example:Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break  

#Example:Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Example:Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Example:Using the range() function:
for x in range(6):
  print(x)

#Example:Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#Example:Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Example:Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x
else:
  print("Finally finished!")

 #Nested loop
#Example:Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) 

# PYTHON FUNCTION
#Creating a Function:In Python a function is defined using the def keyword:
#Example
def my_function():
  print("Hello from a function")

#Calling a Function:To call a function, use the function name followed by parenthesis:
#Example
def my_function():
  print("Hello from a function")

my_function()

#ARGUMENTS
#Example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#NUMBERS OF ARGUMENT
#Example:This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#ARBITARY ARGUMENT
#Example If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Example:If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#DEFAULT PARAMETER VALUE
#Example
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#PASSING A LIST AS AN ARGUMENT
#Example
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#RETURN VALUES
#Example
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#THE PASS STATEMENT
#Example
def myfunction():
  pass
  
#Example
def my_function(x, /):
  print(x)
my_function(3)

#Example
def my_function(x):
  print(x)
my_function(x = 3)

#Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:

#Example
def my_function(*, x):
  print(x)
my_function(x = 3)

