---
draft: true
---

# Learning python by one tiny peice at a time.

# concerns about areas of programming/python that more than one person hasn't been aware of.
# Written from basic to advanced although really everyone should get this.

# How to teach yourself
test = 'example of a string'
testList = ['First list element']
# print(test) # everyone knows this but they don't all use it temporarily to inspect something that isn't working.
type(test) # View variable type python is using, in this case str for string
print(1 + "1") # you get a clear error "unsupported operand type(s) for +: 'int' and 'str'"
# That being, the plus (+) operand in python doesn't know what to do with a number and a string. You might as well be adding 1 + "potato" for all python sees.
print("1" + 1) # More tricky error with "Can't convert 'int' object to str implicitly"
# So what does implicit mean? "not explicit; implied; indirect" or rather. When told to be quite, the threat of detention is implied.
# Thus you can think of print as a function;
def customPrint(*string):
    words = [] # We're going to give a new list of strings back so lets make that list
    for word in string: #loop over everything we're given calling each one "word"
        words.append(str(word)) # add each thing to the list we made but first call str on it.
    return " ".join(words) # Give back a new list of strings joined by the string of whitespace
dir(test) # Look at the methods a certain type exposes to you. You do this to see what things you can do with data you already have.
# Then go a read the python docs about something you don't know or how to use one that looks useful.
# For instance I often forget if append is one p or two, dir([]) and sure enough there's a method with two p's

class myString(str):
   def __str__(s):
     return "example"
testCustomString = myString('Here is a sentence')
repr(testCustomString) # repr is a function to get the actual representation. note this also has the quotes to that denote a string.

print(type(test))
print(dir(test))

# Lists
listOfNumbers = [1,2,3,4,5]
# understand what the index is that's asociated with lists
#index:   0   |   1   |   2   |   3   |   4
#value: <int> | <int> | <int> | <int> | <int>
# thus, listOfNumbers[3] address' the index of the list at position 3, the value of which is 4.
print(listOfNumbers[3]) # 4

# Strings are just a list with letters inside. That's why "Example"[0] returns 'E'.

# Scopes, the idea that variables only exist in certain contexts.
## Many don't see that variables in python exist down and to the right. So every
## Many seem to miss that this total needs to be outside for
total = 0
for num in listOfNumbers:
    total = total + num
print("total should be 15 here: " + str(total) )
# total needs to exist outside of the for block to aggigate the value

name = 'global'
def scopeAExample():
    name = 'scopeB'
    print(name)

def scopeBExample():
    global name
    name = 'scopeB'
    print(name)

print(name) # global
scopeAExample() # scopeA
scopeBExample() # scopeB
print(name) # scopeB
# -------------------

# Objects / dictionary
# I've not seen anyone do this without me explaining it.


# Function calls with parameters and returns.
## Completely forgeign concept to anyone in the class.
def callMe(maybe): ## accept 1 value to the fucntion about to be run, put it in the variable 'maybe'
    return 'I will call: ' + str(maybe) ## Give back a string that also uses the provided value

def callMeBroke(maybe): ## accept 1 value to the fucntion about to be run, put it in the variable 'maybe'
    'I will call: ' + str(maybe) ## Give back a string that also uses the provided value

print( callMe('ishmael') ) ## print whatever callMe gives us back, in this case a string.
print( callMeBroke('Sue') ) ## as callMeBroke doens't return a value, it will implicitaly return the none value type of 'None'
# -------------------


# example problems compounding.
# I see far too much like this that while it does work, demonstrates quite a savere lack of being able to read and UNDERSTAND what is going on.
import csv
with open('learning.py') as datastream:
    for line in datastream:
        # print each line or something
        continue

def searchForLine():
    with open('learning.py') as datastream:
        for line in datastream:
            if line.startswith('#'):
                'this was a comment'
            else:
                'this was code'

# things to note:
# 1. Repeatedly opening the file
# 2. Imports a library but it's never actually used

