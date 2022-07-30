##Modules 3 & 4 Lecture Presentation practice

## FULL LINE COMMENTS ##
# This while line is a comment
# This is another comment line
# All comment lines are ignored by Python
# Even though the next line lools like code, it's just a comment
# x=1
# --------------------------------------------------

## COMMENTS AFTER A LINE OF CODE ##
from operator import index
from matplotlib.cbook import index_of


score = 0 # Initializing the score
price = 9.99
priceWithTax = price * 1.09 # add in 9% tax # Also need a variable for <price>

## MULTILINE COMMENTS ##
'''
A multiline comment starts with a line of three quote
characters (above). This is a long comment block. It can be any length.
you do not need to use the # character here. You end it by entering the
same three quotes you used to start (below)
'''

## GETTING USER INPUT ##
favoritecolor = input('What is your favorite color?')
print('your favorite color is ', favoritecolor)

## STRINGS ##
"This is a string."
'This is also a string.'
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named afdter Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

## COMBINING OR CONCATENATING STRINGS ##
first_name = "James"
last_name = "Bailey"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

## COMBINING OR CONCATENATING STRINGS ##
message = "Hello, " + full_name.title() + "!"
print(message)

## WHAT IS A LIST ##
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


## RELATED DATA ##
# This is a list of test scores:
99
72
88
82
54


## ELEMENTS ##
# This is a shopping list, which is simple list of strings:
'cereal'
'milk'
'orange juice'
'hot dogs'
'gum'

##  PYTHON SYNTAX  ##

shoppingList = ['cereal', 'milk', 'orange juice', 'hot dogs', 'gum']
scoresList = [24, 33, 22, 45, 56, 33, 45]

## MIX OF DATA TYPES  ##

mixedList = [True, 5, 'some string', 123.45]
print(mixedList)
print(type(mixedList))

## EMPTY LIST ##
someList = [] # set a list variable to the empty list - no elements
print(someList)

## LIST INDEX ##


##  ACCESSING ELEMENTS  ##
numbersList = [20, -34, 486, 3129]
numbersList[0] # evaluates to 20
numbersList[1] # evaluates to -34
numbersList[2] # evaluates to 486
numbersList[3] # evaluates to 3129

